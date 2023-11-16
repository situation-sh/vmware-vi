# vmware_vi.ResourcePlanningManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_planning_manager_estimate_database_size**](ResourcePlanningManagerApi.md#resource_planning_manager_estimate_database_size) | **POST** /ResourcePlanningManager/{moId}/EstimateDatabaseSize | Estimates the database size required to store VirtualCenter data. 


# **resource_planning_manager_estimate_database_size**
> DatabaseSizeEstimate resource_planning_manager_estimate_database_size(mo_id, estimate_database_size_request_type)

Estimates the database size required to store VirtualCenter data. 

Estimates the database size required to store VirtualCenter data.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.database_size_estimate import DatabaseSizeEstimate
from vmware_vi.models.estimate_database_size_request_type import EstimateDatabaseSizeRequestType
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
    api_instance = vmware_vi.ResourcePlanningManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    estimate_database_size_request_type = vmware_vi.EstimateDatabaseSizeRequestType() # EstimateDatabaseSizeRequestType | 

    try:
        # Estimates the database size required to store VirtualCenter data. 
        api_response = api_instance.resource_planning_manager_estimate_database_size(mo_id, estimate_database_size_request_type)
        print("The response of ResourcePlanningManagerApi->resource_planning_manager_estimate_database_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcePlanningManagerApi->resource_planning_manager_estimate_database_size: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **estimate_database_size_request_type** | [**EstimateDatabaseSizeRequestType**](EstimateDatabaseSizeRequestType.md)|  | 

### Return type

[**DatabaseSizeEstimate**](DatabaseSizeEstimate.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | *DatabaseSizeEstimate* Returns the size required in MB of the database and the number of database rows.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

