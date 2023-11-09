from typing import Any, Dict, List, Optional, Unpack, Required, Optional, TypedDict, Union, NotRequired,overload
from datetime import datetime

class GetMeasurementParams(TypedDict):
    sort: NotRequired[str]
    id__lt: NotRequired[str]
    id__lte: NotRequired[str]
    id__gt: NotRequired[str]
    id__gte: NotRequired[str]
    id__in: NotRequired[str]
    id: NotRequired[str]
    start_time: NotRequired[datetime]
    start_time__lt: NotRequired[datetime]
    start_time__lte: NotRequired[datetime]
    start_time__gt: NotRequired[datetime]
    start_time__gte: NotRequired[datetime]
    stop_time: NotRequired[datetime]
    stop_time__lt: NotRequired[datetime]
    stop_time__lte: NotRequired[datetime]
    stop_time__gt: NotRequired[datetime]
    stop_time__gte: NotRequired[datetime]
    is_public: NotRequired[bool]
    is_oneoff: NotRequired[bool]
    interval: NotRequired[str]
    interval__lt: NotRequired[str]
    interval__lte: NotRequired[str]
    interval__gt: NotRequired[str]
    interval__gte: NotRequired[str]
    status: NotRequired[str]
    status__in: NotRequired[str]
    tags: NotRequired[str]
    type: NotRequired[str]
    target_ip: NotRequired[str]
    current_probes: NotRequired[str]
    participant_logs_probes: NotRequired[str]
    target_asn: NotRequired[str]
    target: NotRequired[str]
    target__contains: NotRequired[str]
    target__startswith: NotRequired[str]
    target__endswith: NotRequired[str]
    description: NotRequired[str]
    description__contains: NotRequired[str]
    description__startswith: NotRequired[str]
    description__endswith: NotRequired[str]
    af: NotRequired[str]
    search: NotRequired[str]
    protocol: NotRequired[str]
    group_id: NotRequired[str]
    group: NotRequired[str]
    favourite: NotRequired[bool]
    hidden: NotRequired[bool]
    page: NotRequired[int]
    page_size: NotRequired[int]
    after: NotRequired[str]
    format: NotRequired[str]
    callback: NotRequired[str]
    optional_fields: NotRequired[str]
    fields: NotRequired[str]
    format_datetime: NotRequired[str]
    key: NotRequired[str]
    mine: NotRequired[bool]

class MeasurementParams(TypedDict):
    description: Required[str]
    af: Required[int]
    type: Required[str]
    resolve_on_probe: NotRequired[bool]
    is_oneoff: NotRequired[bool]
    start_time: NotRequired[datetime]
    stop_time: NotRequired[datetime]
    interval: NotRequired[int]
    spread: NotRequired[int]
    is_public: NotRequired[bool]

class TracerouteParams(MeasurementParams):
    target: Required[str]
    response_timeout: NotRequired[int]
    packets: NotRequired[int]
    paris: NotRequired[int]
    size: NotRequired[int]
    first_hop: NotRequired[int]
    max_hops: NotRequired[int]
    protocol: NotRequired[str]

class SSLCertParams(MeasurementParams):
    target: Required[str]

class HTTPParams(MeasurementParams):
    target: Required[str]

class NTPParams(MeasurementParams):
    target: Required[str]

class PingParams(MeasurementParams):
    target: Required[str]
    packets: NotRequired[int]
    size: NotRequired[int]
    packet_interval: NotRequired[int]
    include_probe_id: NotRequired[bool]

class DNSParams(MeasurementParams):
    query_class: Required[str]
    query_type: Required[str]
    query_argument: Required[str]
    target_server: NotRequired[str]
    timeout: NotRequired[int]
    udp_payload_size: NotRequired[int]
    retry_times: NotRequired[int]
    protocol: NotRequired[str]
    use_probes_resolver: NotRequired[bool]

class GetProbesParams(TypedDict):
    country_code: NotRequired[str]
    id__lt: NotRequired[int]
    id__lte: NotRequired[int]
    id__gte: NotRequired[int]
    id__gt: NotRequired[int]
    id__in: NotRequired[str]
    latitude: NotRequired[str]
    latitude__lt: NotRequired[str]
    latitude__lte: NotRequired[str]
    latitude__gte: NotRequired[str]
    latitude__gt: NotRequired[str]
    longitude: NotRequired[str]
    longitude__lt: NotRequired[str]
    longitude__lte: NotRequired[str]
    longitude__gte: NotRequired[str]
    longitude__gt: NotRequired[str]
    asn: NotRequired[str]
    asn_v4: NotRequired[str]
    asn_v4__in: NotRequired[str]
    asn_v6: NotRequired[str]
    asn_v6__in: NotRequired[str]
    prefix_v4: NotRequired[str]
    prefix_v6: NotRequired[str]
    status: NotRequired[str]
    status_name: NotRequired[str]
    is_anchor: NotRequired[bool]
    is_public: NotRequired[bool]
    tags: NotRequired[str]
    radius: NotRequired[str]
    country_code__in: NotRequired[str]
    include: NotRequired[str]
    optional_fields: NotRequired[str]
    format: NotRequired[str]
    sort: NotRequired[str]

class ProbeParams(TypedDict):
    requested: Required[int]
    type: Required[str]
    value: Required[Union[str,int]]

