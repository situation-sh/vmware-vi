# vmware_vi.ServiceManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_manager_get_service**](ServiceManagerApi.md#service_manager_get_service) | **GET** /ServiceManager/{moId}/service | The full list of services available in this directory. 
[**service_manager_query_service_list**](ServiceManagerApi.md#service_manager_query_service_list) | **POST** /ServiceManager/{moId}/QueryServiceList | A query interface that returns a list of services that match certain criteria. 


# **service_manager_get_service**
> List[ServiceManagerServiceInfo] service_manager_get_service(mo_id)

The full list of services available in this directory. 

The full list of services available in this directory.  ***Since:*** VI API 2.5  ***Required privileges:*** Global.ServiceManagers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.service_manager_service_info import ServiceManagerServiceInfo
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
    api_instance = vmware_vi.ServiceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The full list of services available in this directory. 
        api_response = api_instance.service_manager_get_service(mo_id)
        print("The response of ServiceManagerApi->service_manager_get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagerApi->service_manager_get_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ServiceManagerServiceInfo]**](ServiceManagerServiceInfo.md)

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

# **service_manager_query_service_list**
> List[ServiceManagerServiceInfo] service_manager_query_service_list(mo_id, query_service_list_request_type)

A query interface that returns a list of services that match certain criteria. 

A query interface that returns a list of services that match certain criteria.  Besides a basic service name entry, an arbitrary list of matching locations can also be specified. The location array is assumed to be a list of AND expressions, ie, all locations must match for an entry to be considered a match. Regular expressions are not allowed in the query service.  ***Since:*** VI API 2.5  ***Required privileges:*** Global.ServiceManagers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_service_list_request_type import QueryServiceListRequestType
from vmware_vi.models.service_manager_service_info import ServiceManagerServiceInfo
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
    api_instance = vmware_vi.ServiceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_service_list_request_type = vmware_vi.QueryServiceListRequestType() # QueryServiceListRequestType | 

    try:
        # A query interface that returns a list of services that match certain criteria. 
        api_response = api_instance.service_manager_query_service_list(mo_id, query_service_list_request_type)
        print("The response of ServiceManagerApi->service_manager_query_service_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagerApi->service_manager_query_service_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_service_list_request_type** | [**QueryServiceListRequestType**](QueryServiceListRequestType.md)|  | 

### Return type

[**List[ServiceManagerServiceInfo]**](ServiceManagerServiceInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

