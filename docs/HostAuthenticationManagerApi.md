# vmware_vi.HostAuthenticationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_authentication_manager_get_info**](HostAuthenticationManagerApi.md#host_authentication_manager_get_info) | **GET** /HostAuthenticationManager/{moId}/info | Information about Active Directory membership. 
[**host_authentication_manager_get_supported_store**](HostAuthenticationManagerApi.md#host_authentication_manager_get_supported_store) | **GET** /HostAuthenticationManager/{moId}/supportedStore | An array that can contain managed object references to local and Active Directory authentication managed objects. 


# **host_authentication_manager_get_info**
> HostAuthenticationManagerInfo host_authentication_manager_get_info(mo_id)

Information about Active Directory membership. 

Information about Active Directory membership.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_authentication_manager_info import HostAuthenticationManagerInfo
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
    api_instance = vmware_vi.HostAuthenticationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about Active Directory membership. 
        api_response = api_instance.host_authentication_manager_get_info(mo_id)
        print("The response of HostAuthenticationManagerApi->host_authentication_manager_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAuthenticationManagerApi->host_authentication_manager_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostAuthenticationManagerInfo**](HostAuthenticationManagerInfo.md)

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

# **host_authentication_manager_get_supported_store**
> List[ManagedObjectReference] host_authentication_manager_get_supported_store(mo_id)

An array that can contain managed object references to local and Active Directory authentication managed objects. 

An array that can contain managed object references to local and Active Directory authentication managed objects.  <code>supportedStore</code> data implies a connection to a system that stores information about accounts. The <code>supportedStore</code> array can include the following objects: - *HostLocalAuthentication* - Local authentication refers   to user accounts on the ESX host. Local authentication is always enabled. - *HostActiveDirectoryAuthentication* - Active Directory authentication   refers to computer accounts and user accounts on the domain controller.   This object indicates the domain membership status for the host   and defines the join and leave methods for Active Directory   membership.      If <code>supportedStore</code> references   a *HostActiveDirectoryAuthentication* object, the host   is capable of joining a domain.   However, if you try to add a host to a domain when the   *HostAuthenticationStoreInfo*.*HostAuthenticationStoreInfo.enabled*   property is <code>True</code> (accessed through the <code>info</code>   property), the join method will throw a fault.    ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
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
    api_instance = vmware_vi.HostAuthenticationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # An array that can contain managed object references to local and Active Directory authentication managed objects. 
        api_response = api_instance.host_authentication_manager_get_supported_store(mo_id)
        print("The response of HostAuthenticationManagerApi->host_authentication_manager_get_supported_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAuthenticationManagerApi->host_authentication_manager_get_supported_store: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *HostAuthenticationStore*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

