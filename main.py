import os
from pathlib import Path
import code

from lndgrpc import LNDClient
from lndgrpc.client import ln

credential_path = Path(os.getenv("CRED_PATH"))

#https://github.com/lightningnetwork/lnd/blob/master/macaroons/README.md



mac = str(credential_path.joinpath("test1234.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

# Create the connection to the remote node
ip_addr = os.getenv("LND_NODE_IP")
lnd = LNDClient(
    f"{ip_addr}:10009",
    macaroon_filepath=mac,
    cert_filepath=tls
)




lncli_mapping = {
    "getinfo": "/lnrpc.Lightning/GetInfo",
    "getrecoveryinfo": "/lnrpc.Lightning/GetRecoveryInfo",
    "debuglevel": "/lnrpc.Lightning/DebugLevel",
    "stop": "/lnrpc.Lightning/StopDaemon",
    "version": "/verrpc.Versioner/GetVersion",
    "sendcustom": "/lnrpc.Lightning/SendCustomMessage",
    "subscribecustom": "/lnrpc.Lightning/SubscribeCustomMessages",
    "openchannel": "/lnrpc.Lightning/OpenChannel",
    "batchopenchannel": "/lnrpc.Lightning/BatchOpenChannel",
    "closechannel": "/lnrpc.Lightning/CloseChannel",
    "closeallchannels": "",
    "abandonchannel": "/lnrpc.Lightning/AbandonChannel",
    "channelbalance": "/lnrpc.Lightning/ChannelBalance",
    "pendingchannels": "/lnrpc.Lightning/PendingChannels",
    "listchannels": "/lnrpc.Lightning/ListChannels",
    "closedchannels": "/lnrpc.Lightning/ClosedChannels",
    "getnetworkinfo": "/lnrpc.Lightning/GetNetworkInfo",
    "feereport": "/lnrpc.Lightning/FeeReport",
    "updatechanpolicy": "/lnrpc.Lightning/UpdateChannelPolicy",
    "exportchanbackup": "/lnrpc.Lightning/",
    "verifychanbackup": "/lnrpc.Lightning/VerifyChanBackup",
    "restorechanbackup": "/lnrpc.Lightning/",
    "updatechanstatus": "/lnrpc.Lightning/",
    "describegraph": "/lnrpc.Lightning/DescribeGraph",
    "getnodemetrics": "/lnrpc.Lightning/GetNodeMetrics",
    "getchaninfo": "/lnrpc.Lightning/GetChanInfo",
    "getnodeinfo": "/lnrpc.Lightning/GetNodeInfo",
    "addinvoice": "/lnrpc.Lightning/AddInvoice",
    "lookupinvoice": "/lnrpc.Lightning/LookupInvoice",
    "listinvoices": "/lnrpc.Lightning/ListInvoices",
    "decodepayreq": "/lnrpc.Lightning/DecodePayReq",
    "bakemacaroon": "/lnrpc.Lightning/BakeMacaroon",
    "listmacaroonids": "/lnrpc.Lightning/ListMacaroonIDs",
    "deletemacaroonid": "/lnrpc.Lightning/",
    "listpermissions": "/lnrpc.Lightning/",
    "printmacaroon": "/lnrpc.Lightning/",
    "constrainmacaroon": "",
    "querymc": "/lnrpc.Router/QueryMissionControl",
    "queryprob": "/lnrpc.Lightning/",
    "resetmc": "",
    "getmccfg": "",
    "setmccfg": "",
    "estimatefee": "/lnrpc.Lightning/EstimateFee",
    "sendmany": "/lnrpc.Lightning/SendMany",
    "sendcoins": "/lnrpc.Lightning/SendCoins",
    "listunspent": "/lnrpc.Lightning/ListUnspent",
    "listchaintxns": "",
    "sendpayment": "/lnrpc.Lightning/SendPayment",
    "payinvoice": "",
    "sendtoroute": "/lnrpc.Lightning/SendToRoute",
    "listpayments": "",
    "queryroutes": "/lnrpc.Lightning/QueryRoutes",
    "fwdinghistory": "/lnrpc.Lightning/ForwardingHistory",
    "trackpayment": "",
    "deletepayments": "/lnrpc.Lightning/DeletePayment",
    "importmc": "",
    "buildroute": "",
    "connect": "/lnrpc.Lightning/ConnectPeer",
    "disconnect": "/lnrpc.Lightning/DisconnectPeer",
    "listpeers": "/lnrpc.Lightning/ListPeers",
    "profile": "",
    "create": "",
    "createwatchonly": "",
    "unlock": "/lnrpc.WalletUnlocker/UnlockWallet",
    "changepassword": "",
    "state": "",
    "newaddress": "/lnrpc.Lightning/NewAddress",
    "walletbalance": "/lnrpc.Lightning/WalletBalance",
    "signmessage": "",
    "verifymessage": "",
    "wtclient": ""
}


rpc_commands = {
    "autopilotrpc.Autopilot": [
        "ModifyStatus",
        "QueryScores",
        "SetScores",
        "Status"
    ],
    "chainrpc.ChainNotifier": [
        "RegisterBlockEpochNtfn",
        "RegisterConfirmationsNtfn",
        "RegisterSpendNtfn"
    ],
    "devrpc.Dev": [
        "ImportGraph"
    ],
    "invoicesrpc.Invoices": [
        "AddHoldInvoice",
        "CancelInvoice",
        "LookupInvoiceV2",
        "SettleInvoice",
        "SubscribeSingleInvoice"
    ],
    "lnrpc.Lightning": [
        "AbandonChannel",
        "AddInvoice",
        "BakeMacaroon",
        "BatchOpenChannel",
        "ChannelAcceptor",
        "ChannelBalance",
        "CheckMacaroonPermissions",
        "CloseChannel",
        "ClosedChannels",
        "ConnectPeer",
        "DebugLevel",
        "DecodePayReq",
        "DeleteAllPayments",
        "DeleteMacaroonID",
        "DeletePayment",
        "DescribeGraph",
        "DisconnectPeer",
        "EstimateFee",
        "ExportAllChannelBackups",
        "ExportChannelBackup",
        "FeeReport",
        "ForwardingHistory",
        "FundingStateStep",
        "GetChanInfo",
        "GetInfo",
        "GetNetworkInfo",
        "GetNodeInfo",
        "GetNodeMetrics",
        "GetRecoveryInfo",
        "GetTransactions",
        "ListChannels",
        "ListInvoices",
        "ListMacaroonIDs",
        "ListPayments",
        "ListPeers",
        "ListPermissions",
        "ListUnspent",
        "LookupInvoice",
        "NewAddress",
        "OpenChannel",
        "OpenChannelSync",
        "PendingChannels",
        "QueryRoutes",
        "RegisterRPCMiddleware",
        "RestoreChannelBackups",
        "SendCoins",
        "SendCustomMessage",
        "SendMany",
        "SendPayment",
        "SendPaymentSync",
        "SendToRoute",
        "SendToRouteSync",
        "SignMessage",
        "StopDaemon",
        "SubscribeChannelBackups",
        "SubscribeChannelEvents",
        "SubscribeChannelGraph",
        "SubscribeCustomMessages",
        "SubscribeInvoices",
        "SubscribePeerEvents",
        "SubscribeTransactions",
        "UpdateChannelPolicy",
        "VerifyChanBackup",
        "VerifyMessage",
        "WalletBalance"
    ],
    "neutrinorpc.NeutrinoKit": [
        "AddPeer",
        "DisconnectPeer",
        "GetBlock",
        "GetBlockHeader",
        "GetCFilter",
        "IsBanned",
        "Status"
    ],
    "peersrpc.Peers": [
        "UpdateNodeAnnouncement"
    ],
    "routerrpc.Router": [
        "BuildRoute",
        "EstimateRouteFee",
        "GetMissionControlConfig",
        "HtlcInterceptor",
        "QueryMissionControl",
        "QueryProbability",
        "ResetMissionControl",
        "SendPayment",
        "SendPaymentV2",
        "SendToRoute",
        "SendToRouteV2",
        "SetMissionControlConfig",
        "SubscribeHtlcEvents",
        "TrackPayment",
        "TrackPaymentV2",
        "UpdateChanStatus",
        "XImportMissionControl"
    ],
    "signrpc.Signer": [
        "ComputeInputScript",
        "DeriveSharedKey",
        "MuSig2Cleanup",
        "MuSig2CombineKeys",
        "MuSig2CombineSig",
        "MuSig2CreateSession",
        "MuSig2RegisterNonces",
        "MuSig2Sign",
        "SignMessage",
        "SignOutputRaw",
        "VerifyMessage"
    ],
    "lnrpc.State": [
        "GetState",
        "SubscribeState"
    ],
    "verrpc.Versioner": [
        "GetVersion"
    ],
    "walletrpc.WalletKit": [
        "BumpFee",
        "DeriveKey",
        "DeriveNextKey",
        "EstimateFee",
        "FinalizePsbt",
        "FundPsbt",
        "ImportAccount",
        "ImportPublicKey",
        "LabelTransaction",
        "LeaseOutput",
        "ListAccounts",
        "ListLeases",
        "ListSweeps",
        "ListUnspent",
        "NextAddr",
        "PendingSweeps",
        "PublishTransaction",
        "ReleaseOutput",
        "RequiredReserve",
        "SendOutputs",
        "SignPsbt"
    ],
    "lnrpc.WalletUnlocker": [
        "ChangePassword",
        "GenSeed",
        "InitWallet",
        "UnlockWallet"
    ],
    "watchtowerrpc.Watchtower": [
        "GetInfo"
    ],
    "wtclientrpc.WatchtowerClient": [
        "AddTower",
        "GetTowerInfo",
        "ListTowers",
        "Policy",
        "RemoveTower",
        "Stats"
    ],
}

def uri_from_subsystem(subsystem):
    for uri_base in rpc_commands:
        if subsystem in uri_base:
            return uri_base

def build_permissions(list_perm_tuple):
    """
    list_perm_tuple = list of tuples
    [ (subsystem1, api_call1), (subsystem2, api_call2), ... ] 
    """
    permissions = []
    for subsystem, api in list_perm_tuple:
        subsystem_full = uri_from_subsystem(subsystem)
        uri = f"/{subsystem_full}/{api}"
        print(uri)
        permissions.append(ln.MacaroonPermission(entity="uri", action=uri))
    return permissions




total_commands = 0
for subsystem in rpc_commands:
    total_commands += len(rpc_commands[subsystem])




r = build_permissions([
    ("Lightning", "GetInfo"),
    ("Lightning", "AddInvoice"),   
])

# ln.MacaroonPermission(entity=,action=)

baked = lnd.bake_macaroon(
    permissions=r,
    root_key_id=7
)

code.interact(local=dict(globals(), **locals()))  


credential_path = Path(credential_path)
baked_mac = credential_path.joinpath("test1234.macaroon")
with open(baked_mac,"wb") as f:
    f.write(bytes.fromhex(baked.macaroon))



lnd.list_macaroon_ids()