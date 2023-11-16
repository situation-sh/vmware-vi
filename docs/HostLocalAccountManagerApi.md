# vmware_vi.HostLocalAccountManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_local_account_manager_assign_user_to_group**](HostLocalAccountManagerApi.md#host_local_account_manager_assign_user_to_group) | **POST** /HostLocalAccountManager/{moId}/AssignUserToGroup | Assigns a user to a group. 
[**host_local_account_manager_change_password**](HostLocalAccountManagerApi.md#host_local_account_manager_change_password) | **POST** /HostLocalAccountManager/{moId}/ChangePassword | Updates the password of a local user account. 
[**host_local_account_manager_create_group**](HostLocalAccountManagerApi.md#host_local_account_manager_create_group) | **POST** /HostLocalAccountManager/{moId}/CreateGroup | Creates a local group account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 
[**host_local_account_manager_create_user**](HostLocalAccountManagerApi.md#host_local_account_manager_create_user) | **POST** /HostLocalAccountManager/{moId}/CreateUser | Creates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 
[**host_local_account_manager_remove_group**](HostLocalAccountManagerApi.md#host_local_account_manager_remove_group) | **POST** /HostLocalAccountManager/{moId}/RemoveGroup | Removes a local group account. 
[**host_local_account_manager_remove_user**](HostLocalAccountManagerApi.md#host_local_account_manager_remove_user) | **POST** /HostLocalAccountManager/{moId}/RemoveUser | Removes a local user account. 
[**host_local_account_manager_unassign_user_from_group**](HostLocalAccountManagerApi.md#host_local_account_manager_unassign_user_from_group) | **POST** /HostLocalAccountManager/{moId}/UnassignUserFromGroup | Unassigns a user from a group. 
[**host_local_account_manager_update_user**](HostLocalAccountManagerApi.md#host_local_account_manager_update_user) | **POST** /HostLocalAccountManager/{moId}/UpdateUser | Updates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 


# **host_local_account_manager_assign_user_to_group**
> host_local_account_manager_assign_user_to_group(mo_id, assign_user_to_group_request_type)

Assigns a user to a group. 

Deprecated as of vSphere API 5.1, local user groups are not supported and group specific methods will throw NotSupported.  Assigns a user to a group.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.assign_user_to_group_request_type import AssignUserToGroupRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    assign_user_to_group_request_type = vmware_vi.AssignUserToGroupRequestType() # AssignUserToGroupRequestType | 

    try:
        # Assigns a user to a group. 
        api_instance.host_local_account_manager_assign_user_to_group(mo_id, assign_user_to_group_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_assign_user_to_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **assign_user_to_group_request_type** | [**AssignUserToGroupRequestType**](AssignUserToGroupRequestType.md)|  | 

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
**500** | ***UserNotFound***: if the specified user or group does not exist.  ***AlreadyExists***: if the user is already a member of the target group.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_change_password**
> host_local_account_manager_change_password(mo_id, change_password_request_type)

Updates the password of a local user account. 

Updates the password of a local user account.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_password_request_type import ChangePasswordRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_password_request_type = vmware_vi.ChangePasswordRequestType() # ChangePasswordRequestType | 

    try:
        # Updates the password of a local user account. 
        api_instance.host_local_account_manager_change_password(mo_id, change_password_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_change_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_password_request_type** | [**ChangePasswordRequestType**](ChangePasswordRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if newPassword has an invalid format.  ***InvalidLogin***: if the user and oldPassword combination is not valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_create_group**
> host_local_account_manager_create_group(mo_id, create_group_request_type)

Creates a local group account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 

Deprecated as of vSphere API 5.1, local user groups are not supported and group specific methods will throw NotSupported.  Creates a local group account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type.  For POSIX hosts, passing the *HostLocalAccountManagerPosixAccountSpecification* data object type allows you to control the group ID format of the group account being created.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_group_request_type import CreateGroupRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_group_request_type = vmware_vi.CreateGroupRequestType() # CreateGroupRequestType | 

    try:
        # Creates a local group account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 
        api_instance.host_local_account_manager_create_group(mo_id, create_group_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_create_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_group_request_type** | [**CreateGroupRequestType**](CreateGroupRequestType.md)|  | 

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
**500** | ***AlreadyExists***: if specified local group already exists.  ***InvalidArgument***: if group name is in invalid format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_create_user**
> host_local_account_manager_create_user(mo_id, create_user_request_type)

Creates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 

Creates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type.  For POSIX hosts, passing *HostLocalAccountManagerPosixAccountSpecification* data object type allows you to control the format of the user ID of the user account being created.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_user_request_type import CreateUserRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_user_request_type = vmware_vi.CreateUserRequestType() # CreateUserRequestType | 

    try:
        # Creates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 
        api_instance.host_local_account_manager_create_user(mo_id, create_user_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_user_request_type** | [**CreateUserRequestType**](CreateUserRequestType.md)|  | 

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
**500** | ***AlreadyExists***: if the specified local user account already exists.  ***InvalidArgument***: if the user name or password has an invalid format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_remove_group**
> host_local_account_manager_remove_group(mo_id, remove_group_request_type)

Removes a local group account. 

Deprecated as of vSphere API 5.1, local user groups are not supported and group specific methods will throw NotSupported.  Removes a local group account.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_group_request_type import RemoveGroupRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_group_request_type = vmware_vi.RemoveGroupRequestType() # RemoveGroupRequestType | 

    try:
        # Removes a local group account. 
        api_instance.host_local_account_manager_remove_group(mo_id, remove_group_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_remove_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_group_request_type** | [**RemoveGroupRequestType**](RemoveGroupRequestType.md)|  | 

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
**500** | ***UserNotFound***: if the specified groupName does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_remove_user**
> host_local_account_manager_remove_user(mo_id, remove_user_request_type)

Removes a local user account. 

Removes a local user account.  As of vSphere API 5.1, this operation will first try to remove all permissions associated with the specified account. The permissions of the user are removed one by one, not atomically, and the operation is not rolled back if the removal of some permission fails.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_user_request_type import RemoveUserRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_user_request_type = vmware_vi.RemoveUserRequestType() # RemoveUserRequestType | 

    try:
        # Removes a local user account. 
        api_instance.host_local_account_manager_remove_user(mo_id, remove_user_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_remove_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_user_request_type** | [**RemoveUserRequestType**](RemoveUserRequestType.md)|  | 

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
**500** | ***SecurityError***: if trying to remove the last local user with DCUI access, or if trying to remove the last local user with full administrative privileges, or if the system has encountered an error while trying to remove user&#39;s permissions. or if the account cannot be removed due to permission issues.  ***UserNotFound***: if the specified userName does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_unassign_user_from_group**
> host_local_account_manager_unassign_user_from_group(mo_id, unassign_user_from_group_request_type)

Unassigns a user from a group. 

Deprecated as of vSphere API 5.1, local user groups are not supported and group specific methods will throw NotSupported.  Unassigns a user from a group.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unassign_user_from_group_request_type import UnassignUserFromGroupRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unassign_user_from_group_request_type = vmware_vi.UnassignUserFromGroupRequestType() # UnassignUserFromGroupRequestType | 

    try:
        # Unassigns a user from a group. 
        api_instance.host_local_account_manager_unassign_user_from_group(mo_id, unassign_user_from_group_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_unassign_user_from_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unassign_user_from_group_request_type** | [**UnassignUserFromGroupRequestType**](UnassignUserFromGroupRequestType.md)|  | 

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
**500** | ***UserNotFound***: if the specified user or group does not exist.  ***NoPermission***: if the group is the only group to which the user belongs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_local_account_manager_update_user**
> host_local_account_manager_update_user(mo_id, update_user_request_type)

Updates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 

Updates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type.  ***Required privileges:*** Host.Local.ManageUserGroups 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_user_request_type import UpdateUserRequestType
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
    api_instance = vmware_vi.HostLocalAccountManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_user_request_type = vmware_vi.UpdateUserRequestType() # UpdateUserRequestType | 

    try:
        # Updates a local user account using the parameters defined in the *HostLocalAccountManagerAccountSpecification* data object type. 
        api_instance.host_local_account_manager_update_user(mo_id, update_user_request_type)
    except Exception as e:
        print("Exception when calling HostLocalAccountManagerApi->host_local_account_manager_update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_user_request_type** | [**UpdateUserRequestType**](UpdateUserRequestType.md)|  | 

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
**500** | ***UserNotFound***: if user is not found.  ***AlreadyExists***: if new account specification specifies an existing user&#39;s ID.  ***InvalidArgument***: if new password or description has an invalid format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

