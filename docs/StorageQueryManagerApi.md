# vmware_vi.StorageQueryManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_query_manager_query_hosts_with_attached_lun**](StorageQueryManagerApi.md#storage_query_manager_query_hosts_with_attached_lun) | **POST** /StorageQueryManager/{moId}/QueryHostsWithAttachedLun | Query the set of all hosts which have the specified lun attached. 


# **storage_query_manager_query_hosts_with_attached_lun**
> List[ManagedObjectReference] storage_query_manager_query_hosts_with_attached_lun(mo_id, query_hosts_with_attached_lun_request_type)

Query the set of all hosts which have the specified lun attached. 

Query the set of all hosts which have the specified lun attached.  Requires Host.Config.Storage privilege on the hosts which have the lun in attached state.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_hosts_with_attached_lun_request_type import QueryHostsWithAttachedLunRequestType
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
    api_instance = vmware_vi.StorageQueryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_hosts_with_attached_lun_request_type = vmware_vi.QueryHostsWithAttachedLunRequestType() # QueryHostsWithAttachedLunRequestType | 

    try:
        # Query the set of all hosts which have the specified lun attached. 
        api_response = api_instance.storage_query_manager_query_hosts_with_attached_lun(mo_id, query_hosts_with_attached_lun_request_type)
        print("The response of StorageQueryManagerApi->storage_query_manager_query_hosts_with_attached_lun:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageQueryManagerApi->storage_query_manager_query_hosts_with_attached_lun: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_hosts_with_attached_lun_request_type** | [**QueryHostsWithAttachedLunRequestType**](QueryHostsWithAttachedLunRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HostSystem The set of hosts which have the specified lun attached. No values are returned if there are no hosts with the specified lun in attached state.  Refers instances of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

