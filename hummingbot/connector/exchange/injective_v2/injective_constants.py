import sys

from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit
from hummingbot.core.data_type.in_flight_order import OrderState

EXCHANGE_NAME = "injective_v2"

DEFAULT_DOMAIN = ""
TESTNET_DOMAIN = "testnet"

DEFAULT_SUBACCOUNT_INDEX = 0
EXTRA_TRANSACTION_GAS = 50000
DEFAULT_GAS_PRICE = 500000000

EXPECTED_BLOCK_TIME = 1
TRANSACTIONS_CHECK_INTERVAL = 3 * EXPECTED_BLOCK_TIME

# Public limit ids
SPOT_MARKETS_LIMIT_ID = "SpotMarkets"
DERIVATIVE_MARKETS_LIMIT_ID = "DerivativeMarkets"
SPOT_ORDERBOOK_LIMIT_ID = "SpotOrderBookSnapshot"
DERIVATIVE_ORDERBOOK_LIMIT_ID = "DerivativeOrderBookSnapshot"
GET_TRANSACTION_INDEXER_LIMIT_ID = "GetTransactionIndexer"
GET_TRANSACTION_CHAIN_LIMIT_ID = "GetTransactionChain"
FUNDING_RATES_LIMIT_ID = "FundingRates"
ORACLE_PRICES_LIMIT_ID = "OraclePrices"
FUNDING_PAYMENTS_LIMIT_ID = "FundingPayments"
GET_SUBACCOUNT_LIMIT_ID = "GetSubaccount"

# Private limit ids
PORTFOLIO_BALANCES_LIMIT_ID = "AccountPortfolio"
POSITIONS_LIMIT_ID = "Positions"
SPOT_ORDERS_HISTORY_LIMIT_ID = "SpotOrdersHistory"
DERIVATIVE_ORDERS_HISTORY_LIMIT_ID = "DerivativeOrdersHistory"
SPOT_TRADES_LIMIT_ID = "SpotTrades"
DERIVATIVE_TRADES_LIMIT_ID = "DerivativeTrades"
SIMULATE_TRANSACTION_LIMIT_ID = "SimulateTransaction"
SEND_TRANSACTION = "SendTransaction"

CHAIN_ENDPOINTS_GROUP_LIMIT_ID = "ChainGroupLimit"
INDEXER_ENDPOINTS_GROUP_LIMIT_ID = "IndexerGroupLimit"

NO_LIMIT = sys.maxsize
ONE_SECOND = 1

ENDPOINTS_RATE_LIMITS = [
    RateLimit(
        limit_id=GET_SUBACCOUNT_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(CHAIN_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=GET_TRANSACTION_CHAIN_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(CHAIN_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SIMULATE_TRANSACTION_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(CHAIN_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SEND_TRANSACTION,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(CHAIN_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SPOT_MARKETS_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=DERIVATIVE_MARKETS_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SPOT_ORDERBOOK_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=DERIVATIVE_ORDERBOOK_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=GET_TRANSACTION_INDEXER_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=PORTFOLIO_BALANCES_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=POSITIONS_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SPOT_ORDERS_HISTORY_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=DERIVATIVE_ORDERS_HISTORY_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=SPOT_TRADES_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=DERIVATIVE_TRADES_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=FUNDING_RATES_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=ORACLE_PRICES_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
    RateLimit(
        limit_id=FUNDING_PAYMENTS_LIMIT_ID,
        limit=NO_LIMIT,
        time_interval=ONE_SECOND,
        linked_limits=[LinkedLimitWeightPair(INDEXER_ENDPOINTS_GROUP_LIMIT_ID)]),
]

PUBLIC_NODE_RATE_LIMITS = [
    RateLimit(limit_id=CHAIN_ENDPOINTS_GROUP_LIMIT_ID, limit=20, time_interval=ONE_SECOND),
    RateLimit(limit_id=INDEXER_ENDPOINTS_GROUP_LIMIT_ID, limit=50, time_interval=ONE_SECOND),
]
PUBLIC_NODE_RATE_LIMITS.extend(ENDPOINTS_RATE_LIMITS)

CUSTOM_NODE_RATE_LIMITS = [
    RateLimit(limit_id=CHAIN_ENDPOINTS_GROUP_LIMIT_ID, limit=NO_LIMIT, time_interval=ONE_SECOND),
    RateLimit(limit_id=INDEXER_ENDPOINTS_GROUP_LIMIT_ID, limit=NO_LIMIT, time_interval=ONE_SECOND),
]
CUSTOM_NODE_RATE_LIMITS.extend(ENDPOINTS_RATE_LIMITS)

ORDER_STATE_MAP = {
    "booked": OrderState.OPEN,
    "partial_filled": OrderState.PARTIALLY_FILLED,
    "filled": OrderState.FILLED,
    "canceled": OrderState.CANCELED,
}

ORDER_NOT_FOUND_ERROR_MESSAGE = "order not found"
ACCOUNT_SEQUENCE_MISMATCH_ERROR = "account sequence mismatch"

BATCH_UPDATE_ORDERS_MESSAGE_TYPE = "/injective.exchange.v1beta1.MsgBatchUpdateOrders"
MARKET_ORDER_MESSAGE_TYPES = [
    "/injective.exchange.v1beta1.MsgCreateSpotMarketOrder",
    "/injective.exchange.v1beta1.MsgCreateDerivativeMarketOrder",
]
