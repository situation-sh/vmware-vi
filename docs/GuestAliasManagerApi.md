# vmware_vi.GuestAliasManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_alias_manager_add_guest_alias**](GuestAliasManagerApi.md#guest_alias_manager_add_guest_alias) | **POST** /GuestAliasManager/{moId}/AddGuestAlias | Defines an alias for a guest account in a virtual machine. 
[**guest_alias_manager_list_guest_aliases**](GuestAliasManagerApi.md#guest_alias_manager_list_guest_aliases) | **POST** /GuestAliasManager/{moId}/ListGuestAliases | Lists the *GuestAliases* for a specified user in the guest that can be used for authentication of guest operations. 
[**guest_alias_manager_list_guest_mapped_aliases**](GuestAliasManagerApi.md#guest_alias_manager_list_guest_mapped_aliases) | **POST** /GuestAliasManager/{moId}/ListGuestMappedAliases | Lists the *GuestMappedAliases* in the guest that can be used for authentication of guest operations. 
[**guest_alias_manager_remove_guest_alias**](GuestAliasManagerApi.md#guest_alias_manager_remove_guest_alias) | **POST** /GuestAliasManager/{moId}/RemoveGuestAlias | Removes an alias from the guest so it can no longer be used for authentication of guest operations. 
[**guest_alias_manager_remove_guest_alias_by_cert**](GuestAliasManagerApi.md#guest_alias_manager_remove_guest_alias_by_cert) | **POST** /GuestAliasManager/{moId}/RemoveGuestAliasByCert | Removes a VMware SSO Server&#39;s certificate and all associated aliases from the guest so it can no longer be used for authentication of guest operations. 


# **guest_alias_manager_add_guest_alias**
> guest_alias_manager_add_guest_alias(mo_id, add_guest_alias_request_type)

Defines an alias for a guest account in a virtual machine. 

Defines an alias for a guest account in a virtual machine.  After the alias is defined, the ESXi Server will use the alias to authenticate guest operations requests.  This will add the given VMware SSO Server's certificate and a subject to the alias store of the specified user in the guest.  In order to add an alias to the guest, you must supply an existing valid credential. This can be any instance of *GuestAuthentication*, but must be valid for the specified guest username.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_guest_alias_request_type import AddGuestAliasRequestType
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
    api_instance = vmware_vi.GuestAliasManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_guest_alias_request_type = vmware_vi.AddGuestAliasRequestType() # AddGuestAliasRequestType | 

    try:
        # Defines an alias for a guest account in a virtual machine. 
        api_instance.guest_alias_manager_add_guest_alias(mo_id, add_guest_alias_request_type)
    except Exception as e:
        print("Exception when calling GuestAliasManagerApi->guest_alias_manager_add_guest_alias: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_guest_alias_request_type** | [**AddGuestAliasRequestType**](AddGuestAliasRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  ***InvalidArgument***: if the operation fails because the certificate is invalid.  ***GuestMultipleMappings***: if the operation fails because mapCert is set and the certificate already exists in the mapping file for a different user.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_alias_manager_list_guest_aliases**
> List[GuestAliases] guest_alias_manager_list_guest_aliases(mo_id, list_guest_aliases_request_type)

Lists the *GuestAliases* for a specified user in the guest that can be used for authentication of guest operations. 

Lists the *GuestAliases* for a specified user in the guest that can be used for authentication of guest operations.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_aliases import GuestAliases
from vmware_vi.models.list_guest_aliases_request_type import ListGuestAliasesRequestType
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
    api_instance = vmware_vi.GuestAliasManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_guest_aliases_request_type = vmware_vi.ListGuestAliasesRequestType() # ListGuestAliasesRequestType | 

    try:
        # Lists the *GuestAliases* for a specified user in the guest that can be used for authentication of guest operations. 
        api_response = api_instance.guest_alias_manager_list_guest_aliases(mo_id, list_guest_aliases_request_type)
        print("The response of GuestAliasManagerApi->guest_alias_manager_list_guest_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestAliasManagerApi->guest_alias_manager_list_guest_aliases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_guest_aliases_request_type** | [**ListGuestAliasesRequestType**](ListGuestAliasesRequestType.md)|  | 

### Return type

[**List[GuestAliases]**](GuestAliases.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_alias_manager_list_guest_mapped_aliases**
> List[GuestMappedAliases] guest_alias_manager_list_guest_mapped_aliases(mo_id, list_guest_mapped_aliases_request_type)

Lists the *GuestMappedAliases* in the guest that can be used for authentication of guest operations. 

Lists the *GuestMappedAliases* in the guest that can be used for authentication of guest operations.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_mapped_aliases import GuestMappedAliases
from vmware_vi.models.list_guest_mapped_aliases_request_type import ListGuestMappedAliasesRequestType
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
    api_instance = vmware_vi.GuestAliasManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_guest_mapped_aliases_request_type = vmware_vi.ListGuestMappedAliasesRequestType() # ListGuestMappedAliasesRequestType | 

    try:
        # Lists the *GuestMappedAliases* in the guest that can be used for authentication of guest operations. 
        api_response = api_instance.guest_alias_manager_list_guest_mapped_aliases(mo_id, list_guest_mapped_aliases_request_type)
        print("The response of GuestAliasManagerApi->guest_alias_manager_list_guest_mapped_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestAliasManagerApi->guest_alias_manager_list_guest_mapped_aliases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_guest_mapped_aliases_request_type** | [**ListGuestMappedAliasesRequestType**](ListGuestMappedAliasesRequestType.md)|  | 

### Return type

[**List[GuestMappedAliases]**](GuestMappedAliases.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_alias_manager_remove_guest_alias**
> guest_alias_manager_remove_guest_alias(mo_id, remove_guest_alias_request_type)

Removes an alias from the guest so it can no longer be used for authentication of guest operations. 

Removes an alias from the guest so it can no longer be used for authentication of guest operations.  It will also be removed from the mapped credentials.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_guest_alias_request_type import RemoveGuestAliasRequestType
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
    api_instance = vmware_vi.GuestAliasManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_guest_alias_request_type = vmware_vi.RemoveGuestAliasRequestType() # RemoveGuestAliasRequestType | 

    try:
        # Removes an alias from the guest so it can no longer be used for authentication of guest operations. 
        api_instance.guest_alias_manager_remove_guest_alias(mo_id, remove_guest_alias_request_type)
    except Exception as e:
        print("Exception when calling GuestAliasManagerApi->guest_alias_manager_remove_guest_alias: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_guest_alias_request_type** | [**RemoveGuestAliasRequestType**](RemoveGuestAliasRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidArgument***: if the operation fails because the certificate is invalid.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_alias_manager_remove_guest_alias_by_cert**
> guest_alias_manager_remove_guest_alias_by_cert(mo_id, remove_guest_alias_by_cert_request_type)

Removes a VMware SSO Server's certificate and all associated aliases from the guest so it can no longer be used for authentication of guest operations. 

Removes a VMware SSO Server's certificate and all associated aliases from the guest so it can no longer be used for authentication of guest operations.  It will also be removed from the global certificate-to-user mapping file in the guest.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_guest_alias_by_cert_request_type import RemoveGuestAliasByCertRequestType
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
    api_instance = vmware_vi.GuestAliasManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_guest_alias_by_cert_request_type = vmware_vi.RemoveGuestAliasByCertRequestType() # RemoveGuestAliasByCertRequestType | 

    try:
        # Removes a VMware SSO Server's certificate and all associated aliases from the guest so it can no longer be used for authentication of guest operations. 
        api_instance.guest_alias_manager_remove_guest_alias_by_cert(mo_id, remove_guest_alias_by_cert_request_type)
    except Exception as e:
        print("Exception when calling GuestAliasManagerApi->guest_alias_manager_remove_guest_alias_by_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_guest_alias_by_cert_request_type** | [**RemoveGuestAliasByCertRequestType**](RemoveGuestAliasByCertRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***InvalidArgument***: if the operation fails because the certificate is invalid.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

