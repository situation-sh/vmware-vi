# vmware_vi.HostAccessManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_access_manager_change_access_mode**](HostAccessManagerApi.md#host_access_manager_change_access_mode) | **POST** /HostAccessManager/{moId}/ChangeAccessMode | Update the access mode for a user or group. 
[**host_access_manager_change_lockdown_mode**](HostAccessManagerApi.md#host_access_manager_change_lockdown_mode) | **POST** /HostAccessManager/{moId}/ChangeLockdownMode | Changes the lockdown state of the ESXi host. 
[**host_access_manager_get_lockdown_mode**](HostAccessManagerApi.md#host_access_manager_get_lockdown_mode) | **GET** /HostAccessManager/{moId}/lockdownMode | Current lockdown state of the host. 
[**host_access_manager_query_lockdown_exceptions**](HostAccessManagerApi.md#host_access_manager_query_lockdown_exceptions) | **POST** /HostAccessManager/{moId}/QueryLockdownExceptions | Get the list of users which are exceptions for lockdown mode. 
[**host_access_manager_query_system_users**](HostAccessManagerApi.md#host_access_manager_query_system_users) | **POST** /HostAccessManager/{moId}/QuerySystemUsers | Get the list of local system users. 
[**host_access_manager_retrieve_host_access_control_entries**](HostAccessManagerApi.md#host_access_manager_retrieve_host_access_control_entries) | **POST** /HostAccessManager/{moId}/RetrieveHostAccessControlEntries | Retrieve access entries. 
[**host_access_manager_update_lockdown_exceptions**](HostAccessManagerApi.md#host_access_manager_update_lockdown_exceptions) | **POST** /HostAccessManager/{moId}/UpdateLockdownExceptions | Update the list of users which are exceptions for lockdown mode. 
[**host_access_manager_update_system_users**](HostAccessManagerApi.md#host_access_manager_update_system_users) | **POST** /HostAccessManager/{moId}/UpdateSystemUsers | Update the list of local system users. 


# **host_access_manager_change_access_mode**
> host_access_manager_change_access_mode(mo_id, change_access_mode_request_type)

Update the access mode for a user or group. 

Update the access mode for a user or group.  If the host is in lockdown mode, this operation is allowed only on users in the exceptions list - see *HostAccessManager.QueryLockdownExceptions*, and trying to change the access mode of other users or groups will fail with SecurityError.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_access_mode_request_type import ChangeAccessModeRequestType
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_access_mode_request_type = vmware_vi.ChangeAccessModeRequestType() # ChangeAccessModeRequestType | 

    try:
        # Update the access mode for a user or group. 
        api_instance.host_access_manager_change_access_mode(mo_id, change_access_mode_request_type)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_change_access_mode: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_access_mode_request_type** | [**ChangeAccessModeRequestType**](ChangeAccessModeRequestType.md)|  | 

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
**500** | ***AuthMinimumAdminPermission***: if this change would render the ESXi host inaccessible for local non-system users. The API *HostAccessManager.ChangeLockdownMode* may be used instead.  ***InvalidArgument***: if accessMode is not valid.  ***SecurityError***: if the host is in lockdown mode and &#39;principal&#39; is not in the exceptions list.  ***UserNotFound***: if the specified user is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_change_lockdown_mode**
> host_access_manager_change_lockdown_mode(mo_id, change_lockdown_mode_request_type)

Changes the lockdown state of the ESXi host. 

Changes the lockdown state of the ESXi host.  This operation will do nothing if the host is already in the desired lockdown state.  When the host is in lockdown mode it can be managed only through vCenter and through DCUI (Direct Console User Interface) if the DCUI service is running. This is achieved by removing all permissions on the host, except those of the exception users defined with *HostAccessManager.UpdateLockdownExceptions*.  In addition, the permissions for users 'dcui' and 'vpxuser' are always preserved.  When lockdown mode is disabled, the system will try to restore all permissions that have been removed when lockdown mode was enabled. It is possible that not all permissions may be restored and this is not an error, e.g. if in the meantime some user or managed object was deleted.  It may be possible that after exiting lockdown mode the only permissions on the host will be those of users 'dcui' and 'vpxuser'. This will render the host unmanageable if it is not already managed by vCenter, or if the connection to vCenter is lost. To prevent this, the users in the \"DCUI.Access\" list will be assigned Admin roles.  While the host is in lockdown mode, some operations will fail with SecurityError. This ensures that the conditions for lockdown mode cannot be changed. For example it is allowed to change the access mode only for users in the exceptions list.  When the host is in lockdown mode, changing the running state of service DCUI through *HostServiceSystem* will also fail with SecurityError accompanied with an appropriate localizeable message.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_lockdown_mode_request_type import ChangeLockdownModeRequestType
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_lockdown_mode_request_type = vmware_vi.ChangeLockdownModeRequestType() # ChangeLockdownModeRequestType | 

    try:
        # Changes the lockdown state of the ESXi host. 
        api_instance.host_access_manager_change_lockdown_mode(mo_id, change_lockdown_mode_request_type)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_change_lockdown_mode: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_lockdown_mode_request_type** | [**ChangeLockdownModeRequestType**](ChangeLockdownModeRequestType.md)|  | 

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
**500** | ***AuthMinimumAdminPermission***: if the user invoking the operation is not in the exceptions list - see *HostAccessManager.QueryLockdownExceptions*.  ***NoPermission***: if the current session does not have enough permissions to perform the operation.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_get_lockdown_mode**
> HostLockdownModeEnum host_access_manager_get_lockdown_mode(mo_id)

Current lockdown state of the host. 

Current lockdown state of the host.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_lockdown_mode_enum import HostLockdownModeEnum
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current lockdown state of the host. 
        api_response = api_instance.host_access_manager_get_lockdown_mode(mo_id)
        print("The response of HostAccessManagerApi->host_access_manager_get_lockdown_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_get_lockdown_mode: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostLockdownModeEnum**](HostLockdownModeEnum.md)

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

# **host_access_manager_query_lockdown_exceptions**
> List[str] host_access_manager_query_lockdown_exceptions(mo_id)

Get the list of users which are exceptions for lockdown mode. 

Get the list of users which are exceptions for lockdown mode.  See *HostAccessManager.UpdateLockdownExceptions*.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the list of users which are exceptions for lockdown mode. 
        api_response = api_instance.host_access_manager_query_lockdown_exceptions(mo_id)
        print("The response of HostAccessManagerApi->host_access_manager_query_lockdown_exceptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_query_lockdown_exceptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of users which will not lose their permissions when the host enters lockdown mode.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_query_system_users**
> List[str] host_access_manager_query_system_users(mo_id)

Get the list of local system users. 

Get the list of local system users.  These are special users like 'vpxuser' and 'dcui', which may be used for authenticating different sub-components of the vSphere system and may be essential for its correct functioning.  Usually these users may not be used by human operators to connect directly to the host and the UI may choose to show them only in some \"advanced\" UI view.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the list of local system users. 
        api_response = api_instance.host_access_manager_query_system_users(mo_id)
        print("The response of HostAccessManagerApi->host_access_manager_query_system_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_query_system_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of local system users.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_retrieve_host_access_control_entries**
> List[HostAccessControlEntry] host_access_manager_retrieve_host_access_control_entries(mo_id)

Retrieve access entries. 

Retrieve access entries.  Returns a list of AccessEntry objects for each VIM user or group which have explicitly assigned permissions on the host. This means that *accessNone* will not be present in the result.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_access_control_entry import HostAccessControlEntry
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieve access entries. 
        api_response = api_instance.host_access_manager_retrieve_host_access_control_entries(mo_id)
        print("The response of HostAccessManagerApi->host_access_manager_retrieve_host_access_control_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_retrieve_host_access_control_entries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostAccessControlEntry]**](HostAccessControlEntry.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of AccessEntry objects.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_update_lockdown_exceptions**
> host_access_manager_update_lockdown_exceptions(mo_id, update_lockdown_exceptions_request_type)

Update the list of users which are exceptions for lockdown mode. 

Update the list of users which are exceptions for lockdown mode.  Usually these are user accounts used by third party solutions and external applications which need to continue to function in lockdown mode. It is not advised to add user accounts used by human operators, because this will compromise the purpose of lockdown mode.  Both local and domain users are supported. The format for domain accounts is \"DOMAIN\\\\login\".  When this API is called when the host is in lockdown mode, the behaviour is as follows: - if a user is removed from the exceptions list,   then the permissions of that user are removed. - if a user is added to the exceptions list,   then the permissions of that user are restored.    ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_lockdown_exceptions_request_type import UpdateLockdownExceptionsRequestType
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_lockdown_exceptions_request_type = vmware_vi.UpdateLockdownExceptionsRequestType() # UpdateLockdownExceptionsRequestType | 

    try:
        # Update the list of users which are exceptions for lockdown mode. 
        api_instance.host_access_manager_update_lockdown_exceptions(mo_id, update_lockdown_exceptions_request_type)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_update_lockdown_exceptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_lockdown_exceptions_request_type** | [**UpdateLockdownExceptionsRequestType**](UpdateLockdownExceptionsRequestType.md)|  | 

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
**500** | ***AuthMinimumAdminPermission***: if the user invoking the operation is not present in the new list of exceptions.  ***UserNotFound***: if one of the specified users is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_access_manager_update_system_users**
> host_access_manager_update_system_users(mo_id, update_system_users_request_type)

Update the list of local system users. 

Update the list of local system users.  The special users 'dcui' and 'vpxuser' need not be specified. They are always reported in the list of system users.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Global.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_system_users_request_type import UpdateSystemUsersRequestType
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
    api_instance = vmware_vi.HostAccessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_system_users_request_type = vmware_vi.UpdateSystemUsersRequestType() # UpdateSystemUsersRequestType | 

    try:
        # Update the list of local system users. 
        api_instance.host_access_manager_update_system_users(mo_id, update_system_users_request_type)
    except Exception as e:
        print("Exception when calling HostAccessManagerApi->host_access_manager_update_system_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_system_users_request_type** | [**UpdateSystemUsersRequestType**](UpdateSystemUsersRequestType.md)|  | 

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
**500** | ***InvalidArgument***: If one of the specified user names is not valid, or is in Active Directory domain format.  ***UserNotFound***: If one of the specified users is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

