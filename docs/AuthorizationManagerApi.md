# vmware_vi.AuthorizationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorization_manager_add_authorization_role**](AuthorizationManagerApi.md#authorization_manager_add_authorization_role) | **POST** /AuthorizationManager/{moId}/AddAuthorizationRole | Adds a new role. 
[**authorization_manager_fetch_user_privilege_on_entities**](AuthorizationManagerApi.md#authorization_manager_fetch_user_privilege_on_entities) | **POST** /AuthorizationManager/{moId}/FetchUserPrivilegeOnEntities | Get the list of effective privileges for a user, either granted explicitly, or through group membership. 
[**authorization_manager_get_description**](AuthorizationManagerApi.md#authorization_manager_get_description) | **GET** /AuthorizationManager/{moId}/description | Static, descriptive strings for system roles and privileges. 
[**authorization_manager_get_privilege_list**](AuthorizationManagerApi.md#authorization_manager_get_privilege_list) | **GET** /AuthorizationManager/{moId}/privilegeList | The list of system-defined privileges. 
[**authorization_manager_get_role_list**](AuthorizationManagerApi.md#authorization_manager_get_role_list) | **GET** /AuthorizationManager/{moId}/roleList | The currently defined roles in the system, including static system-defined roles. 
[**authorization_manager_has_privilege_on_entities**](AuthorizationManagerApi.md#authorization_manager_has_privilege_on_entities) | **POST** /AuthorizationManager/{moId}/HasPrivilegeOnEntities | Check whether a session holds a set of privileges on a set of managed entities. 
[**authorization_manager_has_privilege_on_entity**](AuthorizationManagerApi.md#authorization_manager_has_privilege_on_entity) | **POST** /AuthorizationManager/{moId}/HasPrivilegeOnEntity | Check whether a session holds a set of privileges on a managed entity. 
[**authorization_manager_has_user_privilege_on_entities**](AuthorizationManagerApi.md#authorization_manager_has_user_privilege_on_entities) | **POST** /AuthorizationManager/{moId}/HasUserPrivilegeOnEntities | Checks if a user holds a certain set of privileges on a number of managed entities. 
[**authorization_manager_merge_permissions**](AuthorizationManagerApi.md#authorization_manager_merge_permissions) | **POST** /AuthorizationManager/{moId}/MergePermissions | Reassigns all permissions of a role to another role. 
[**authorization_manager_remove_authorization_role**](AuthorizationManagerApi.md#authorization_manager_remove_authorization_role) | **POST** /AuthorizationManager/{moId}/RemoveAuthorizationRole | Removes a role. 
[**authorization_manager_remove_entity_permission**](AuthorizationManagerApi.md#authorization_manager_remove_entity_permission) | **POST** /AuthorizationManager/{moId}/RemoveEntityPermission | Removes a permission rule from an entity. 
[**authorization_manager_reset_entity_permissions**](AuthorizationManagerApi.md#authorization_manager_reset_entity_permissions) | **POST** /AuthorizationManager/{moId}/ResetEntityPermissions | Update the entire set of permissions defined on an entity. 
[**authorization_manager_retrieve_all_permissions**](AuthorizationManagerApi.md#authorization_manager_retrieve_all_permissions) | **POST** /AuthorizationManager/{moId}/RetrieveAllPermissions | Finds all permissions defined in the system. 
[**authorization_manager_retrieve_entity_permissions**](AuthorizationManagerApi.md#authorization_manager_retrieve_entity_permissions) | **POST** /AuthorizationManager/{moId}/RetrieveEntityPermissions | Gets permissions defined on or effective on a managed entity. 
[**authorization_manager_retrieve_role_permissions**](AuthorizationManagerApi.md#authorization_manager_retrieve_role_permissions) | **POST** /AuthorizationManager/{moId}/RetrieveRolePermissions | Finds all the permissions that use a particular role. 
[**authorization_manager_set_entity_permissions**](AuthorizationManagerApi.md#authorization_manager_set_entity_permissions) | **POST** /AuthorizationManager/{moId}/SetEntityPermissions | Defines one or more permission rules on an entity or updates rules if already present for the given user or group on the entity. 
[**authorization_manager_update_authorization_role**](AuthorizationManagerApi.md#authorization_manager_update_authorization_role) | **POST** /AuthorizationManager/{moId}/UpdateAuthorizationRole | Updates a role&#39;s name or privileges. 


# **authorization_manager_add_authorization_role**
> int authorization_manager_add_authorization_role(mo_id, add_authorization_role_request_type)

Adds a new role. 

Adds a new role.  This method will add a user-defined role with given list of privileges and three system-defined privileges, \"System.Anonymous\", \"System.View\", and \"System.Read\".  ***Required privileges:*** Authorization.ModifyRoles 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_authorization_role_request_type import AddAuthorizationRoleRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_authorization_role_request_type = vmware_vi.AddAuthorizationRoleRequestType() # AddAuthorizationRoleRequestType | 

    try:
        # Adds a new role. 
        api_response = api_instance.authorization_manager_add_authorization_role(mo_id, add_authorization_role_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_add_authorization_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_add_authorization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_authorization_role_request_type** | [**AddAuthorizationRoleRequestType**](AddAuthorizationRoleRequestType.md)|  | 

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
**200** | The roleId assigned to the new role.  |  -  |
**500** | ***AlreadyExists***: if a role with the given name already exists.  ***InvalidName***: if the role name is empty.  ***InvalidArgument***: if privIds contains an unknown privilege.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_fetch_user_privilege_on_entities**
> List[UserPrivilegeResult] authorization_manager_fetch_user_privilege_on_entities(mo_id, fetch_user_privilege_on_entities_request_type)

Get the list of effective privileges for a user, either granted explicitly, or through group membership. 

Get the list of effective privileges for a user, either granted explicitly, or through group membership.  This API is implemented only by vCenter Server.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.fetch_user_privilege_on_entities_request_type import FetchUserPrivilegeOnEntitiesRequestType
from vmware_vi.models.user_privilege_result import UserPrivilegeResult
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    fetch_user_privilege_on_entities_request_type = vmware_vi.FetchUserPrivilegeOnEntitiesRequestType() # FetchUserPrivilegeOnEntitiesRequestType | 

    try:
        # Get the list of effective privileges for a user, either granted explicitly, or through group membership. 
        api_response = api_instance.authorization_manager_fetch_user_privilege_on_entities(mo_id, fetch_user_privilege_on_entities_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_fetch_user_privilege_on_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_fetch_user_privilege_on_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **fetch_user_privilege_on_entities_request_type** | [**FetchUserPrivilegeOnEntitiesRequestType**](FetchUserPrivilegeOnEntitiesRequestType.md)|  | 

### Return type

[**List[UserPrivilegeResult]**](UserPrivilegeResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the privilege check result for each entity  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_get_description**
> AuthorizationDescription authorization_manager_get_description(mo_id)

Static, descriptive strings for system roles and privileges. 

Static, descriptive strings for system roles and privileges.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.authorization_description import AuthorizationDescription
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Static, descriptive strings for system roles and privileges. 
        api_response = api_instance.authorization_manager_get_description(mo_id)
        print("The response of AuthorizationManagerApi->authorization_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**AuthorizationDescription**](AuthorizationDescription.md)

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

# **authorization_manager_get_privilege_list**
> List[AuthorizationPrivilege] authorization_manager_get_privilege_list(mo_id)

The list of system-defined privileges. 

The list of system-defined privileges.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.authorization_privilege import AuthorizationPrivilege
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of system-defined privileges. 
        api_response = api_instance.authorization_manager_get_privilege_list(mo_id)
        print("The response of AuthorizationManagerApi->authorization_manager_get_privilege_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_get_privilege_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AuthorizationPrivilege]**](AuthorizationPrivilege.md)

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

# **authorization_manager_get_role_list**
> List[AuthorizationRole] authorization_manager_get_role_list(mo_id)

The currently defined roles in the system, including static system-defined roles. 

The currently defined roles in the system, including static system-defined roles.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.authorization_role import AuthorizationRole
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The currently defined roles in the system, including static system-defined roles. 
        api_response = api_instance.authorization_manager_get_role_list(mo_id)
        print("The response of AuthorizationManagerApi->authorization_manager_get_role_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_get_role_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AuthorizationRole]**](AuthorizationRole.md)

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

# **authorization_manager_has_privilege_on_entities**
> List[EntityPrivilege] authorization_manager_has_privilege_on_entities(mo_id, has_privilege_on_entities_request_type)

Check whether a session holds a set of privileges on a set of managed entities. 

Check whether a session holds a set of privileges on a set of managed entities.  If the session does not exist, false is returned for all privileges of all the entities.  This API is implemented only by vCenter Server.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.entity_privilege import EntityPrivilege
from vmware_vi.models.has_privilege_on_entities_request_type import HasPrivilegeOnEntitiesRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    has_privilege_on_entities_request_type = vmware_vi.HasPrivilegeOnEntitiesRequestType() # HasPrivilegeOnEntitiesRequestType | 

    try:
        # Check whether a session holds a set of privileges on a set of managed entities. 
        api_response = api_instance.authorization_manager_has_privilege_on_entities(mo_id, has_privilege_on_entities_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_has_privilege_on_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_has_privilege_on_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **has_privilege_on_entities_request_type** | [**HasPrivilegeOnEntitiesRequestType**](HasPrivilegeOnEntitiesRequestType.md)|  | 

### Return type

[**List[EntityPrivilege]**](EntityPrivilege.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The privilege check result.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_has_privilege_on_entity**
> List[bool] authorization_manager_has_privilege_on_entity(mo_id, has_privilege_on_entity_request_type)

Check whether a session holds a set of privileges on a managed entity. 

Check whether a session holds a set of privileges on a managed entity.  If the session does not exist, false is returned for all privileges.  This API is implemented only by vCenter Server.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.has_privilege_on_entity_request_type import HasPrivilegeOnEntityRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    has_privilege_on_entity_request_type = vmware_vi.HasPrivilegeOnEntityRequestType() # HasPrivilegeOnEntityRequestType | 

    try:
        # Check whether a session holds a set of privileges on a managed entity. 
        api_response = api_instance.authorization_manager_has_privilege_on_entity(mo_id, has_privilege_on_entity_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_has_privilege_on_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_has_privilege_on_entity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **has_privilege_on_entity_request_type** | [**HasPrivilegeOnEntityRequestType**](HasPrivilegeOnEntityRequestType.md)|  | 

### Return type

**List[bool]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a boolean value for each privilege indicating whether the session holds the privilege.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_has_user_privilege_on_entities**
> List[EntityPrivilege] authorization_manager_has_user_privilege_on_entities(mo_id, has_user_privilege_on_entities_request_type)

Checks if a user holds a certain set of privileges on a number of managed entities. 

Checks if a user holds a certain set of privileges on a number of managed entities.  Privileges may be granted to users through their respective group membership. If a privilege is granted to a group it is implicitly granted to its members.  This API is implemented only by vCenter Server.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.entity_privilege import EntityPrivilege
from vmware_vi.models.has_user_privilege_on_entities_request_type import HasUserPrivilegeOnEntitiesRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    has_user_privilege_on_entities_request_type = vmware_vi.HasUserPrivilegeOnEntitiesRequestType() # HasUserPrivilegeOnEntitiesRequestType | 

    try:
        # Checks if a user holds a certain set of privileges on a number of managed entities. 
        api_response = api_instance.authorization_manager_has_user_privilege_on_entities(mo_id, has_user_privilege_on_entities_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_has_user_privilege_on_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_has_user_privilege_on_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **has_user_privilege_on_entities_request_type** | [**HasUserPrivilegeOnEntitiesRequestType**](HasUserPrivilegeOnEntitiesRequestType.md)|  | 

### Return type

[**List[EntityPrivilege]**](EntityPrivilege.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the privilege check result  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_merge_permissions**
> authorization_manager_merge_permissions(mo_id, merge_permissions_request_type)

Reassigns all permissions of a role to another role. 

Reassigns all permissions of a role to another role.  ***Required privileges:*** Authorization.ReassignRolePermissions 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.merge_permissions_request_type import MergePermissionsRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    merge_permissions_request_type = vmware_vi.MergePermissionsRequestType() # MergePermissionsRequestType | 

    try:
        # Reassigns all permissions of a role to another role. 
        api_instance.authorization_manager_merge_permissions(mo_id, merge_permissions_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_merge_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **merge_permissions_request_type** | [**MergePermissionsRequestType**](MergePermissionsRequestType.md)|  | 

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
**500** | ***NotFound***: if either the source or destination role does not exist.  ***InvalidArgument***: if dstRoleId is the View or Anonymous role or if both role IDs are the same.  ***AuthMinimumAdminPermission***: if srcRoleId is the Administrator role, meaning that applying the change would leave the system with no Administrator permission on the root node.  ***NoPermission***: if current session does not have any privilege in the source or destination role or \&quot;Authorization.ReassignRolePermissions\&quot; privilege on the root folder.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_remove_authorization_role**
> authorization_manager_remove_authorization_role(mo_id, remove_authorization_role_request_type)

Removes a role. 

Removes a role.  ***Required privileges:*** Authorization.ModifyRoles 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_authorization_role_request_type import RemoveAuthorizationRoleRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_authorization_role_request_type = vmware_vi.RemoveAuthorizationRoleRequestType() # RemoveAuthorizationRoleRequestType | 

    try:
        # Removes a role. 
        api_instance.authorization_manager_remove_authorization_role(mo_id, remove_authorization_role_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_remove_authorization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_authorization_role_request_type** | [**RemoveAuthorizationRoleRequestType**](RemoveAuthorizationRoleRequestType.md)|  | 

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
**500** | ***NotFound***: if the role does not exist.  ***InvalidArgument***: if the role is a system role, meaning it cannot be changed.  ***RemoveFailed***: if failIfUsed is true and the role has permissions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_remove_entity_permission**
> authorization_manager_remove_entity_permission(mo_id, remove_entity_permission_request_type)

Removes a permission rule from an entity. 

Removes a permission rule from an entity.  This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.  This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_entity_permission_request_type import RemoveEntityPermissionRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_entity_permission_request_type = vmware_vi.RemoveEntityPermissionRequestType() # RemoveEntityPermissionRequestType | 

    try:
        # Removes a permission rule from an entity. 
        api_instance.authorization_manager_remove_entity_permission(mo_id, remove_entity_permission_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_remove_entity_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_entity_permission_request_type** | [**RemoveEntityPermissionRequestType**](RemoveEntityPermissionRequestType.md)|  | 

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
**500** | ***NotFound***: if a permission for this entity and user or group does not exist.  ***AuthMinimumAdminPermission***: if this change would leave the system with no Administrator permission on the root node.  ***InvalidArgument***: if one of the new role IDs is the View or Anonymous role, or the entity does not support removing permissions.  ***NoPermission***: if current session does not have any privilege in the permission to be removed or \&quot;Authorization.ModifyPermissions\&quot; privilege on the entity.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_reset_entity_permissions**
> authorization_manager_reset_entity_permissions(mo_id, reset_entity_permissions_request_type)

Update the entire set of permissions defined on an entity. 

Update the entire set of permissions defined on an entity.  Any existing permissions on the entity are removed and replaced with the provided set.  If a permission is specified multiple times for the same user or group, the last permission specified takes effect.  The operation is transactional per permission and could partially fail. The updates are performed in the order of the permission array argument. The first failed update will abort the operation and throw the appropriate exception. When the operation aborts, any permissions that have not yet been removed are left in their original state.  After updates are applied, original permissions that are not in the new set are removed. A failure to remove a permission, such as a violation of the minimum administrator permission rule, will abort the operation and could leave remaining original permissions still effective on the entity.  This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.  This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reset_entity_permissions_request_type import ResetEntityPermissionsRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reset_entity_permissions_request_type = vmware_vi.ResetEntityPermissionsRequestType() # ResetEntityPermissionsRequestType | 

    try:
        # Update the entire set of permissions defined on an entity. 
        api_instance.authorization_manager_reset_entity_permissions(mo_id, reset_entity_permissions_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_reset_entity_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reset_entity_permissions_request_type** | [**ResetEntityPermissionsRequestType**](ResetEntityPermissionsRequestType.md)|  | 

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
**500** | ***ManagedObjectNotFound***: if the given entity does not exist.  ***UserNotFound***: if one of the given users or groups does not exist.  ***NotFound***: if a permission for this entity and user or group does not exist.  ***AuthMinimumAdminPermission***: if this change would leave the system with no Administrator permission on the root node, or it would grant further permission to a user or group who already has Administrator permission on the root node.  ***InvalidArgument***: if one of the new role IDs is the View or Anonymous role, or the entity does not support assigning permissions.  ***NoPermission***: if current session does not have any privilege in the updated permission or \&quot;Authorization.ModifyPermissions\&quot; privilege on the entity.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_retrieve_all_permissions**
> List[Permission] authorization_manager_retrieve_all_permissions(mo_id)

Finds all permissions defined in the system. 

Finds all permissions defined in the system.  The result is restricted to the managed entities visible to the user making the call.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.permission import Permission
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Finds all permissions defined in the system. 
        api_response = api_instance.authorization_manager_retrieve_all_permissions(mo_id)
        print("The response of AuthorizationManagerApi->authorization_manager_retrieve_all_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_retrieve_all_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Permission]**](Permission.md)

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

# **authorization_manager_retrieve_entity_permissions**
> List[Permission] authorization_manager_retrieve_entity_permissions(mo_id, retrieve_entity_permissions_request_type)

Gets permissions defined on or effective on a managed entity. 

Gets permissions defined on or effective on a managed entity.  This returns the actual permission objects defined in the system for all users and groups relative to the managed entity. The inherited flag specifies whether or not to include permissions defined by the parents of this entity that propagate to this entity.  For complex entities, the entity reported as defining the permission may be either the parent or a child entity belonging to the complex entity.  The purpose of this method is to discover permissions for administration purposes, not to determine the current permissions. The current user's permissions are found on the *ManagedEntity.effectiveRole* property of the user's ManagedEntity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.permission import Permission
from vmware_vi.models.retrieve_entity_permissions_request_type import RetrieveEntityPermissionsRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_entity_permissions_request_type = vmware_vi.RetrieveEntityPermissionsRequestType() # RetrieveEntityPermissionsRequestType | 

    try:
        # Gets permissions defined on or effective on a managed entity. 
        api_response = api_instance.authorization_manager_retrieve_entity_permissions(mo_id, retrieve_entity_permissions_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_retrieve_entity_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_retrieve_entity_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_entity_permissions_request_type** | [**RetrieveEntityPermissionsRequestType**](RetrieveEntityPermissionsRequestType.md)|  | 

### Return type

[**List[Permission]**](Permission.md)

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

# **authorization_manager_retrieve_role_permissions**
> List[Permission] authorization_manager_retrieve_role_permissions(mo_id, retrieve_role_permissions_request_type)

Finds all the permissions that use a particular role. 

Finds all the permissions that use a particular role.  The result is restricted to managed entities that are visible to the user making the call.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.permission import Permission
from vmware_vi.models.retrieve_role_permissions_request_type import RetrieveRolePermissionsRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_role_permissions_request_type = vmware_vi.RetrieveRolePermissionsRequestType() # RetrieveRolePermissionsRequestType | 

    try:
        # Finds all the permissions that use a particular role. 
        api_response = api_instance.authorization_manager_retrieve_role_permissions(mo_id, retrieve_role_permissions_request_type)
        print("The response of AuthorizationManagerApi->authorization_manager_retrieve_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_retrieve_role_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_role_permissions_request_type** | [**RetrieveRolePermissionsRequestType**](RetrieveRolePermissionsRequestType.md)|  | 

### Return type

[**List[Permission]**](Permission.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotFound***: if the role does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_set_entity_permissions**
> authorization_manager_set_entity_permissions(mo_id, set_entity_permissions_request_type)

Defines one or more permission rules on an entity or updates rules if already present for the given user or group on the entity. 

Defines one or more permission rules on an entity or updates rules if already present for the given user or group on the entity.  If a permission is specified multiple times for the same user or group, then the last permission specified takes effect.  The operation is applied transactionally per permission and is applied to the entity following the order of the elements in the permission array argument. This means that if a failure occurs, the method terminates at that point in the permission array with an exception, leaving at least one and as many as all permissions unapplied.  This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.  This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_entity_permissions_request_type import SetEntityPermissionsRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_entity_permissions_request_type = vmware_vi.SetEntityPermissionsRequestType() # SetEntityPermissionsRequestType | 

    try:
        # Defines one or more permission rules on an entity or updates rules if already present for the given user or group on the entity. 
        api_instance.authorization_manager_set_entity_permissions(mo_id, set_entity_permissions_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_set_entity_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_entity_permissions_request_type** | [**SetEntityPermissionsRequestType**](SetEntityPermissionsRequestType.md)|  | 

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
**500** | ***ManagedObjectNotFound***: if the given entity does not exist.  ***UserNotFound***: if a given user or group does not exist.  ***AuthMinimumAdminPermission***: if this change would leave the system with no Administrator permission on the root node, or it would grant further permission to a user or group who already has Administrator permission on the root node.  ***NotFound***: if a permission&#39;s roleId is not valid.  ***InvalidArgument***: if one of the new role IDs is the View or Anonymous role, or the entity does not support assigning permissions.  ***NoPermission***: if current session does not have any privilege in any permission that being set or \&quot;Authorization.ModifyPermissions\&quot; privilege on the entity.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_manager_update_authorization_role**
> authorization_manager_update_authorization_role(mo_id, update_authorization_role_request_type)

Updates a role's name or privileges. 

Updates a role's name or privileges.  If the new set of privileges are assigned to the role, the system-defined privileges, \"System.Anonymous\", \"System.View\", and \"System.Read\" will be assigned to the role too. This operation might return before the new privileges are effective. A timeout of 100 ms is possible, but it might vary depending on the configuration and the load of the system.  ***Required privileges:*** Authorization.ModifyRoles 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_authorization_role_request_type import UpdateAuthorizationRoleRequestType
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
    api_instance = vmware_vi.AuthorizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_authorization_role_request_type = vmware_vi.UpdateAuthorizationRoleRequestType() # UpdateAuthorizationRoleRequestType | 

    try:
        # Updates a role's name or privileges. 
        api_instance.authorization_manager_update_authorization_role(mo_id, update_authorization_role_request_type)
    except Exception as e:
        print("Exception when calling AuthorizationManagerApi->authorization_manager_update_authorization_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_authorization_role_request_type** | [**UpdateAuthorizationRoleRequestType**](UpdateAuthorizationRoleRequestType.md)|  | 

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
**500** | ***NotFound***: if the role does not exist, or if a privilege in the list cannot be found.  ***InvalidArgument***: if the role is a system role, meaning it cannot be changed.  ***InvalidName***: if the new role name is empty.  ***AlreadyExists***: if another role with the given name already exists.  ***NoPermission***: if current session does not have any privilege that being updated in the new role or \&quot;Authorization.ModifyRoles\&quot; privilege on the root folder.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

