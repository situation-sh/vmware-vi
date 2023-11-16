# vmware_vi.PerformanceManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**performance_manager_create_perf_interval**](PerformanceManagerApi.md#performance_manager_create_perf_interval) | **POST** /PerformanceManager/{moId}/CreatePerfInterval | Adds a new historical interval. 
[**performance_manager_get_description**](PerformanceManagerApi.md#performance_manager_get_description) | **GET** /PerformanceManager/{moId}/description | The static description strings. 
[**performance_manager_get_historical_interval**](PerformanceManagerApi.md#performance_manager_get_historical_interval) | **GET** /PerformanceManager/{moId}/historicalInterval | A list of *intervals* configured on the system. 
[**performance_manager_get_perf_counter**](PerformanceManagerApi.md#performance_manager_get_perf_counter) | **GET** /PerformanceManager/{moId}/perfCounter | A list of all supported performance counters in the system. 
[**performance_manager_query_available_perf_metric**](PerformanceManagerApi.md#performance_manager_query_available_perf_metric) | **POST** /PerformanceManager/{moId}/QueryAvailablePerfMetric | Retrieves all performance counters for the specified *managed object* generated during a specified period of time. 
[**performance_manager_query_perf**](PerformanceManagerApi.md#performance_manager_query_perf) | **POST** /PerformanceManager/{moId}/QueryPerf | Retrieves the performance metrics for the specified entity (or entities) based on the properties specified in the *PerfQuerySpec* data object. 
[**performance_manager_query_perf_composite**](PerformanceManagerApi.md#performance_manager_query_perf_composite) | **POST** /PerformanceManager/{moId}/QueryPerfComposite | Retrieves a *PerfCompositeMetric* data object that comprises statistics for the specified entity and its children entities. 
[**performance_manager_query_perf_counter**](PerformanceManagerApi.md#performance_manager_query_perf_counter) | **POST** /PerformanceManager/{moId}/QueryPerfCounter | Retrieves counter information for the specified list of counter IDs. 
[**performance_manager_query_perf_counter_by_level**](PerformanceManagerApi.md#performance_manager_query_perf_counter_by_level) | **POST** /PerformanceManager/{moId}/QueryPerfCounterByLevel | Retrieves the set of counters that are available at a specified collection *PerfInterval.level*. 
[**performance_manager_query_perf_provider_summary**](PerformanceManagerApi.md#performance_manager_query_perf_provider_summary) | **POST** /PerformanceManager/{moId}/QueryPerfProviderSummary | Retrieves the *PerfProviderSummary* data object that defines the capabilities of the specified managed object with respect to statistics, such as whether it supports current or summary statistics&amp;#46; 
[**performance_manager_remove_perf_interval**](PerformanceManagerApi.md#performance_manager_remove_perf_interval) | **POST** /PerformanceManager/{moId}/RemovePerfInterval | Removes an interval from the list. 
[**performance_manager_reset_counter_level_mapping**](PerformanceManagerApi.md#performance_manager_reset_counter_level_mapping) | **POST** /PerformanceManager/{moId}/ResetCounterLevelMapping | Restores a set of performance counters to the default level of data collection. 
[**performance_manager_update_counter_level_mapping**](PerformanceManagerApi.md#performance_manager_update_counter_level_mapping) | **POST** /PerformanceManager/{moId}/UpdateCounterLevelMapping | Changes the level of data collection for a set of performance counters. 
[**performance_manager_update_perf_interval**](PerformanceManagerApi.md#performance_manager_update_perf_interval) | **POST** /PerformanceManager/{moId}/UpdatePerfInterval | Modifies VirtualCenter Server&#39;s built-in *historical intervals*, within certain limits. 


# **performance_manager_create_perf_interval**
> performance_manager_create_perf_interval(mo_id, create_perf_interval_request_type)

Adds a new historical interval. 

Deprecated as of API 2.5, use *PerformanceManager.UpdatePerfInterval*. The default historical intervals can be modified, but they cannot be created.  Adds a new historical interval.  Sampling period for new interval must be a multiple of an existing interval; must comprise a longer period of time; and must be uniquely named.  ***Required privileges:*** Performance.ModifyIntervals 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_perf_interval_request_type import CreatePerfIntervalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_perf_interval_request_type = vmware_vi.CreatePerfIntervalRequestType() # CreatePerfIntervalRequestType | 

    try:
        # Adds a new historical interval. 
        api_instance.performance_manager_create_perf_interval(mo_id, create_perf_interval_request_type)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_create_perf_interval: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_perf_interval_request_type** | [**CreatePerfIntervalRequestType**](CreatePerfIntervalRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_get_description**
> PerformanceDescription performance_manager_get_description(mo_id)

The static description strings. 

The static description strings.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.performance_description import PerformanceDescription
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The static description strings. 
        api_response = api_instance.performance_manager_get_description(mo_id)
        print("The response of PerformanceManagerApi->performance_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**PerformanceDescription**](PerformanceDescription.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_get_historical_interval**
> List[PerfInterval] performance_manager_get_historical_interval(mo_id)

A list of *intervals* configured on the system. 

A list of *intervals* configured on the system.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_interval import PerfInterval
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of *intervals* configured on the system. 
        api_response = api_instance.performance_manager_get_historical_interval(mo_id)
        print("The response of PerformanceManagerApi->performance_manager_get_historical_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_get_historical_interval: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[PerfInterval]**](PerfInterval.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_get_perf_counter**
> List[PerfCounterInfo] performance_manager_get_perf_counter(mo_id)

A list of all supported performance counters in the system. 

A list of all supported performance counters in the system.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_counter_info import PerfCounterInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of all supported performance counters in the system. 
        api_response = api_instance.performance_manager_get_perf_counter(mo_id)
        print("The response of PerformanceManagerApi->performance_manager_get_perf_counter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_get_perf_counter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[PerfCounterInfo]**](PerfCounterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_available_perf_metric**
> List[PerfMetricId] performance_manager_query_available_perf_metric(mo_id, query_available_perf_metric_request_type)

Retrieves all performance counters for the specified *managed object* generated during a specified period of time. 

Retrieves all performance counters for the specified *managed object* generated during a specified period of time.  The time period can be specified using beginTime, endTime, or by interval ID.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_metric_id import PerfMetricId
from vmware_vi.models.query_available_perf_metric_request_type import QueryAvailablePerfMetricRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_available_perf_metric_request_type = vmware_vi.QueryAvailablePerfMetricRequestType() # QueryAvailablePerfMetricRequestType | 

    try:
        # Retrieves all performance counters for the specified *managed object* generated during a specified period of time. 
        api_response = api_instance.performance_manager_query_available_perf_metric(mo_id, query_available_perf_metric_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_available_perf_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_available_perf_metric: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_available_perf_metric_request_type** | [**QueryAvailablePerfMetricRequestType**](QueryAvailablePerfMetricRequestType.md)|  | 

### Return type

[**List[PerfMetricId]**](PerfMetricId.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of metrics, each of which comprises a *PerfMetricId.counterId* and an *name*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_perf**
> List[PerfEntityMetricBase] performance_manager_query_perf(mo_id, query_perf_request_type)

Retrieves the performance metrics for the specified entity (or entities) based on the properties specified in the *PerfQuerySpec* data object. 

Retrieves the performance metrics for the specified entity (or entities) based on the properties specified in the *PerfQuerySpec* data object.  **Query Performance for VirtualCenter Server**    ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_entity_metric_base import PerfEntityMetricBase
from vmware_vi.models.query_perf_request_type import QueryPerfRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_perf_request_type = vmware_vi.QueryPerfRequestType() # QueryPerfRequestType | 

    try:
        # Retrieves the performance metrics for the specified entity (or entities) based on the properties specified in the *PerfQuerySpec* data object. 
        api_response = api_instance.performance_manager_query_perf(mo_id, query_perf_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_perf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_perf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_perf_request_type** | [**QueryPerfRequestType**](QueryPerfRequestType.md)|  | 

### Return type

[**List[PerfEntityMetricBase]**](PerfEntityMetricBase.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metric values for the specified entity or entities.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_perf_composite**
> PerfCompositeMetric performance_manager_query_perf_composite(mo_id, query_perf_composite_request_type)

Retrieves a *PerfCompositeMetric* data object that comprises statistics for the specified entity and its children entities. 

Retrieves a *PerfCompositeMetric* data object that comprises statistics for the specified entity and its children entities.  Only metrics for the first level of descendents are included in the *PerfCompositeMetric* object.  Use this operation to obtain statistics for a *host* and its associated *virtual machines*, for example.  Requires **system.read** privilege for every virtual machine on the target host, or the query fails with the &#147;NoPermission&#148; fault. Suported for *HostSystem* managed entities only.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_composite_metric import PerfCompositeMetric
from vmware_vi.models.query_perf_composite_request_type import QueryPerfCompositeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_perf_composite_request_type = vmware_vi.QueryPerfCompositeRequestType() # QueryPerfCompositeRequestType | 

    try:
        # Retrieves a *PerfCompositeMetric* data object that comprises statistics for the specified entity and its children entities. 
        api_response = api_instance.performance_manager_query_perf_composite(mo_id, query_perf_composite_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_perf_composite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_perf_composite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_perf_composite_request_type** | [**QueryPerfCompositeRequestType**](QueryPerfCompositeRequestType.md)|  | 

### Return type

[**PerfCompositeMetric**](PerfCompositeMetric.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metric values for the specified entity and its associated entities for a single interval.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_perf_counter**
> List[PerfCounterInfo] performance_manager_query_perf_counter(mo_id, query_perf_counter_request_type)

Retrieves counter information for the specified list of counter IDs. 

Retrieves counter information for the specified list of counter IDs.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_counter_info import PerfCounterInfo
from vmware_vi.models.query_perf_counter_request_type import QueryPerfCounterRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_perf_counter_request_type = vmware_vi.QueryPerfCounterRequestType() # QueryPerfCounterRequestType | 

    try:
        # Retrieves counter information for the specified list of counter IDs. 
        api_response = api_instance.performance_manager_query_perf_counter(mo_id, query_perf_counter_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_perf_counter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_perf_counter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_perf_counter_request_type** | [**QueryPerfCounterRequestType**](QueryPerfCounterRequestType.md)|  | 

### Return type

[**List[PerfCounterInfo]**](PerfCounterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array consisting of performance counter information for the specified counterIds.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_perf_counter_by_level**
> List[PerfCounterInfo] performance_manager_query_perf_counter_by_level(mo_id, query_perf_counter_by_level_request_type)

Retrieves the set of counters that are available at a specified collection *PerfInterval.level*. 

Retrieves the set of counters that are available at a specified collection *PerfInterval.level*.  The collection level determines the statistics that get stored in VirtualCenter. See *PerfInterval* for more information about VirtualCenter Server historical statistics collection.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_counter_info import PerfCounterInfo
from vmware_vi.models.query_perf_counter_by_level_request_type import QueryPerfCounterByLevelRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_perf_counter_by_level_request_type = vmware_vi.QueryPerfCounterByLevelRequestType() # QueryPerfCounterByLevelRequestType | 

    try:
        # Retrieves the set of counters that are available at a specified collection *PerfInterval.level*. 
        api_response = api_instance.performance_manager_query_perf_counter_by_level(mo_id, query_perf_counter_by_level_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_perf_counter_by_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_perf_counter_by_level: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_perf_counter_by_level_request_type** | [**QueryPerfCounterByLevelRequestType**](QueryPerfCounterByLevelRequestType.md)|  | 

### Return type

[**List[PerfCounterInfo]**](PerfCounterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of *PerfCounterInfo* objects that define the set of counters having the specified level number available for the entity.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_query_perf_provider_summary**
> PerfProviderSummary performance_manager_query_perf_provider_summary(mo_id, query_perf_provider_summary_request_type)

Retrieves the *PerfProviderSummary* data object that defines the capabilities of the specified managed object with respect to statistics, such as whether it supports current or summary statistics&#46; 

Retrieves the *PerfProviderSummary* data object that defines the capabilities of the specified managed object with respect to statistics, such as whether it supports current or summary statistics&#46;  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perf_provider_summary import PerfProviderSummary
from vmware_vi.models.query_perf_provider_summary_request_type import QueryPerfProviderSummaryRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_perf_provider_summary_request_type = vmware_vi.QueryPerfProviderSummaryRequestType() # QueryPerfProviderSummaryRequestType | 

    try:
        # Retrieves the *PerfProviderSummary* data object that defines the capabilities of the specified managed object with respect to statistics, such as whether it supports current or summary statistics&#46; 
        api_response = api_instance.performance_manager_query_perf_provider_summary(mo_id, query_perf_provider_summary_request_type)
        print("The response of PerformanceManagerApi->performance_manager_query_perf_provider_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_query_perf_provider_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_perf_provider_summary_request_type** | [**QueryPerfProviderSummaryRequestType**](QueryPerfProviderSummaryRequestType.md)|  | 

### Return type

[**PerfProviderSummary**](PerfProviderSummary.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data object containing metadata about the entity as a performance provider, such as the type of metrics (real-time, summary, or both) it generates and the *PerfProviderSummary.refreshRate*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_remove_perf_interval**
> performance_manager_remove_perf_interval(mo_id, remove_perf_interval_request_type)

Removes an interval from the list. 

Deprecated as of API 2.5, use *PerformanceManager.UpdatePerfInterval*. Historical intervals cannot be removed.  Removes an interval from the list.  ***Required privileges:*** Performance.ModifyIntervals 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_perf_interval_request_type import RemovePerfIntervalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_perf_interval_request_type = vmware_vi.RemovePerfIntervalRequestType() # RemovePerfIntervalRequestType | 

    try:
        # Removes an interval from the list. 
        api_instance.performance_manager_remove_perf_interval(mo_id, remove_perf_interval_request_type)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_remove_perf_interval: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_perf_interval_request_type** | [**RemovePerfIntervalRequestType**](RemovePerfIntervalRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_reset_counter_level_mapping**
> performance_manager_reset_counter_level_mapping(mo_id, reset_counter_level_mapping_request_type)

Restores a set of performance counters to the default level of data collection. 

Restores a set of performance counters to the default level of data collection.  See the <a href=\"#counterTables\">performance counter tables</a> for the default collection level for individual counters.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Performance.ModifyIntervals 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reset_counter_level_mapping_request_type import ResetCounterLevelMappingRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reset_counter_level_mapping_request_type = vmware_vi.ResetCounterLevelMappingRequestType() # ResetCounterLevelMappingRequestType | 

    try:
        # Restores a set of performance counters to the default level of data collection. 
        api_instance.performance_manager_reset_counter_level_mapping(mo_id, reset_counter_level_mapping_request_type)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_reset_counter_level_mapping: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reset_counter_level_mapping_request_type** | [**ResetCounterLevelMappingRequestType**](ResetCounterLevelMappingRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_update_counter_level_mapping**
> performance_manager_update_counter_level_mapping(mo_id, update_counter_level_mapping_request_type)

Changes the level of data collection for a set of performance counters. 

Changes the level of data collection for a set of performance counters.  See the <a href=\"#counterTables\">performance counter tables</a> for the default collection level for individual counters.  **Important:**  Consider the performance and storage consequences of using this method. You may cause a significant increase in data collection and storage, along with a corresponding decrease in performance. vCenter Server performance and database storage requirements depend on the collection levels defined for the performance intervals (PerformanceManager.*PerformanceManager.historicalInterval*) and the collection levels specified for individual performance counters (*PerfCounterInfo*.*PerfCounterInfo.level*).  <u>Performance Counter Data Collection</u>  vSphere defines four levels of data collection for performance counters. Each performance counter specifies a level for collection. The historical performance intervals (PerformanceManager.*PerformanceManager.historicalInterval*) define the sampling period and length for a particular collection level.  The amount of data collected for a performance counter depends on the performance interval and on the type of entity for which the counter is defined. For example, a datastore counter such as datastoreIops (the aggregate number of IO operations on the datastore) will generate a data set that corresponds to the number of datastores on a host. If a vCenter Server manages a large number of hosts with a large number of datastores, the Server will collect a large amount of data.  There are other counters for which the vCenter Server collects a relatively smaller amount of data. For example, memory counters are collected as a single counter per virtual machine and a single counter per host.  <u>Performance Counter Data Storage</u>  The performance interval collection *PerfCounterInfo.level* defines the set of counters for which the vCenter Server stores performance data. The Server will store data for counters at the specified level and for counters at all lower levels.  By default, all the performance intervals specify collection level one. Using these defaults, the vCenter Server stores performance counter data in the vCenter database for all counters that specify collection level one. It does not store data for counters that specify collection levels two through four.  <u>Performance Manager Method Interaction</u>  You can use the UpdateCounterLevelMapping method to change the collection level for individual counters. You can also use the *PerformanceManager.UpdatePerfInterval* method to change the collection level for the system-defined performance intervals. These methods can cause a significant increase in the amount of data collected and stored in the vCenter database.  You may cause a significant increase in data collection and storage along with a corresponding decrease in performance under the following conditions: - By default the system-defined performance intervals use collection   level one, storing data for all counters that specify collection   level one. If you use the UpdateCounterLevelMapping method to change   the collection level of performance counters to level one, you will   increase the amount of stored performance data. - If you use the *PerformanceManager.UpdatePerfInterval* method to increase   the collection level for the system-defined performance intervals,   you will increase the amount of stored performance data.     To restore counter levels to default settings use the *PerformanceManager.ResetCounterLevelMapping* method.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Performance.ModifyIntervals 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_counter_level_mapping_request_type import UpdateCounterLevelMappingRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_counter_level_mapping_request_type = vmware_vi.UpdateCounterLevelMappingRequestType() # UpdateCounterLevelMappingRequestType | 

    try:
        # Changes the level of data collection for a set of performance counters. 
        api_instance.performance_manager_update_counter_level_mapping(mo_id, update_counter_level_mapping_request_type)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_update_counter_level_mapping: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_counter_level_mapping_request_type** | [**UpdateCounterLevelMappingRequestType**](UpdateCounterLevelMappingRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_manager_update_perf_interval**
> performance_manager_update_perf_interval(mo_id, update_perf_interval_request_type)

Modifies VirtualCenter Server's built-in *historical intervals*, within certain limits. 

Modifies VirtualCenter Server's built-in *historical intervals*, within certain limits.  **Supported Modifications** <table border=\"1\"width=\"100%\"> <tr> <th>key</th> <th>samplingPeriod</th> <th>length</th> <th>name</th> <th>level \\[1\\]</th> <th>enabled \\[2\\]</th> </tr> <tr> <td>1</td> <td>300 \\[3\\]</td> <td>86400 \\[4\\]</td> <td>Past&nbsp;day</td> <td>1</td> <td>true</td> </tr> <tr> <td>2</td> <td>1800</td> <td>604800</td> <td>Past&nbsp;week</td> <td>1</td> <td>true</td> </tr> <tr> <td>3</td> <td>7200</td> <td>2592000</td> <td>Past&nbsp;month</td> <td>1</td> <td>true</td> </tr> <tr> <td>4</td> <td>86400</td> <td>31536000 \\[5\\]</td> <td>Past&nbsp;year</td> <td>1</td> <td>true</td> </tr> </table>  **\\[1\\]**&nbsp; The collection level for the *historical intervals* can be changed. However, the level specified for a lower-numbered interval cannot be smaller than that of a larger interval.   **\\[2\\]**&nbsp; An interval can be disabled. By default, all four intervals are enabled. Disabling an interval disables all higher intervals. For example, disabling interval 3 (&#147;Past month&#148;) also disables interval 4 (&#147;Past year&#148;).   **\\[3\\]**&nbsp; Can reduce this interval&#146;s *PerfInterval.samplingPeriod* from 5 minutes to 1, 2, or 3 minutes.   **\\[4\\]**&nbsp; Can increase this interval&#146;s *PerfInterval.length* from 1 day to 2 or 3 days.   **\\[5\\]**&nbsp; Can increase interval&#146;s *PerfInterval.length* from 1 year to 2 or 3 years.    See *PerfInterval* for information about the four default intervals for VirtualCenter Server.  ***Required privileges:*** Performance.ModifyIntervals 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_perf_interval_request_type import UpdatePerfIntervalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.PerformanceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_perf_interval_request_type = vmware_vi.UpdatePerfIntervalRequestType() # UpdatePerfIntervalRequestType | 

    try:
        # Modifies VirtualCenter Server's built-in *historical intervals*, within certain limits. 
        api_instance.performance_manager_update_perf_interval(mo_id, update_perf_interval_request_type)
    except Exception as e:
        print("Exception when calling PerformanceManagerApi->performance_manager_update_perf_interval: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_perf_interval_request_type** | [**UpdatePerfIntervalRequestType**](UpdatePerfIntervalRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

