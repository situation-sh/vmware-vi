# vmware_vi.GuestAuthManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_auth_manager_acquire_credentials_in_guest**](GuestAuthManagerApi.md#guest_auth_manager_acquire_credentials_in_guest) | **POST** /GuestAuthManager/{moId}/AcquireCredentialsInGuest | Authenticates in the guest and returns a *GuestAuthentication* object with the acquired credentials for use in subsequent guest operation calls. 
[**guest_auth_manager_release_credentials_in_guest**](GuestAuthManagerApi.md#guest_auth_manager_release_credentials_in_guest) | **POST** /GuestAuthManager/{moId}/ReleaseCredentialsInGuest | Releases session data and resources associated with a *GuestAuthentication* object returned by *GuestAuthManager.AcquireCredentialsInGuest*. 
[**guest_auth_manager_validate_credentials_in_guest**](GuestAuthManagerApi.md#guest_auth_manager_validate_credentials_in_guest) | **POST** /GuestAuthManager/{moId}/ValidateCredentialsInGuest | Validates the *GuestAuthentication* credentials. 


# **guest_auth_manager_acquire_credentials_in_guest**
> GuestAuthentication guest_auth_manager_acquire_credentials_in_guest(mo_id, acquire_credentials_in_guest_request_type)

Authenticates in the guest and returns a *GuestAuthentication* object with the acquired credentials for use in subsequent guest operation calls. 

Authenticates in the guest and returns a *GuestAuthentication* object with the acquired credentials for use in subsequent guest operation calls.  This can be used to authenticate inside the guest and obtain a *GuestAuthentication* object for supported authentication types. This operation is not needed for Name and Password Authentication. To use Name and Password Authentication, see *NamePasswordAuthentication*. For SSPI authentication, requestAuth should be of the type *SSPIAuthentication*.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.acquire_credentials_in_guest_request_type import AcquireCredentialsInGuestRequestType
from vmware_vi.models.guest_authentication import GuestAuthentication
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
    api_instance = vmware_vi.GuestAuthManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    acquire_credentials_in_guest_request_type = vmware_vi.AcquireCredentialsInGuestRequestType() # AcquireCredentialsInGuestRequestType | 

    try:
        # Authenticates in the guest and returns a *GuestAuthentication* object with the acquired credentials for use in subsequent guest operation calls. 
        api_response = api_instance.guest_auth_manager_acquire_credentials_in_guest(mo_id, acquire_credentials_in_guest_request_type)
        print("The response of GuestAuthManagerApi->guest_auth_manager_acquire_credentials_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestAuthManagerApi->guest_auth_manager_acquire_credentials_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **acquire_credentials_in_guest_request_type** | [**AcquireCredentialsInGuestRequestType**](AcquireCredentialsInGuestRequestType.md)|  | 

### Return type

[**GuestAuthentication**](GuestAuthentication.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a *GuestAuthentication* object that can be used in guest operation calls.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestAuthenticationChallenge***: if the credential information provided requires a challenge to authenticate.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  ***TooManyGuestLogons***: if there are too many concurrent login sessions active in the guest.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_auth_manager_release_credentials_in_guest**
> guest_auth_manager_release_credentials_in_guest(mo_id, release_credentials_in_guest_request_type)

Releases session data and resources associated with a *GuestAuthentication* object returned by *GuestAuthManager.AcquireCredentialsInGuest*. 

Releases session data and resources associated with a *GuestAuthentication* object returned by *GuestAuthManager.AcquireCredentialsInGuest*.  This frees any resources and session data associated with a *GuestAuthentication* object returned by *GuestAuthManager.AcquireCredentialsInGuest*. The *GuestAuthentication* object can no longer be used to authenticate in the guest once released. Currently this operation is only valid for *TicketedSessionAuthentication* objects.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.release_credentials_in_guest_request_type import ReleaseCredentialsInGuestRequestType
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
    api_instance = vmware_vi.GuestAuthManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    release_credentials_in_guest_request_type = vmware_vi.ReleaseCredentialsInGuestRequestType() # ReleaseCredentialsInGuestRequestType | 

    try:
        # Releases session data and resources associated with a *GuestAuthentication* object returned by *GuestAuthManager.AcquireCredentialsInGuest*. 
        api_instance.guest_auth_manager_release_credentials_in_guest(mo_id, release_credentials_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestAuthManagerApi->guest_auth_manager_release_credentials_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **release_credentials_in_guest_request_type** | [**ReleaseCredentialsInGuestRequestType**](ReleaseCredentialsInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_auth_manager_validate_credentials_in_guest**
> guest_auth_manager_validate_credentials_in_guest(mo_id, validate_credentials_in_guest_request_type)

Validates the *GuestAuthentication* credentials. 

Validates the *GuestAuthentication* credentials.  This can be used to check the authentication data, or validate any authentication that has a timeout is still valid. If the authentication is not valid, *GuestPermissionDenied* will be thrown.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.validate_credentials_in_guest_request_type import ValidateCredentialsInGuestRequestType
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
    api_instance = vmware_vi.GuestAuthManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    validate_credentials_in_guest_request_type = vmware_vi.ValidateCredentialsInGuestRequestType() # ValidateCredentialsInGuestRequestType | 

    try:
        # Validates the *GuestAuthentication* credentials. 
        api_instance.guest_auth_manager_validate_credentials_in_guest(mo_id, validate_credentials_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestAuthManagerApi->guest_auth_manager_validate_credentials_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **validate_credentials_in_guest_request_type** | [**ValidateCredentialsInGuestRequestType**](ValidateCredentialsInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

