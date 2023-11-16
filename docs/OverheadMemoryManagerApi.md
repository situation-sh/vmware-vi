# vmware_vi.OverheadMemoryManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**overhead_memory_manager_lookup_vm_overhead_memory**](OverheadMemoryManagerApi.md#overhead_memory_manager_lookup_vm_overhead_memory) | **POST** /OverheadMemoryManager/{moId}/LookupVmOverheadMemory | Return static VM overhead memory value in bytes for a (vm, host) pair from the overhead memory module (OMM) in Virtual Center. 


# **overhead_memory_manager_lookup_vm_overhead_memory**
> int overhead_memory_manager_lookup_vm_overhead_memory(mo_id, lookup_vm_overhead_memory_request_type)

Return static VM overhead memory value in bytes for a (vm, host) pair from the overhead memory module (OMM) in Virtual Center. 

Return static VM overhead memory value in bytes for a (vm, host) pair from the overhead memory module (OMM) in Virtual Center.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.lookup_vm_overhead_memory_request_type import LookupVmOverheadMemoryRequestType
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
    api_instance = vmware_vi.OverheadMemoryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    lookup_vm_overhead_memory_request_type = vmware_vi.LookupVmOverheadMemoryRequestType() # LookupVmOverheadMemoryRequestType | 

    try:
        # Return static VM overhead memory value in bytes for a (vm, host) pair from the overhead memory module (OMM) in Virtual Center. 
        api_response = api_instance.overhead_memory_manager_lookup_vm_overhead_memory(mo_id, lookup_vm_overhead_memory_request_type)
        print("The response of OverheadMemoryManagerApi->overhead_memory_manager_lookup_vm_overhead_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadMemoryManagerApi->overhead_memory_manager_lookup_vm_overhead_memory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **lookup_vm_overhead_memory_request_type** | [**LookupVmOverheadMemoryRequestType**](LookupVmOverheadMemoryRequestType.md)|  | 

### Return type

**int**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Overhead memory value, if found in the OMM.  |  -  |
**500** | ***NotFound***: If the overhead memory value is not found in the OMM.  ***InvalidType***: If the MoRefs do not point to appropriate type of inventory objects - VM and Host respectively.  ***InvalidArgument***: If any of the MoRefs are NULL.  ***ManagedObjectNotFound***: If the inventory objects cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

