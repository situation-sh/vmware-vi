# vmware_vi.UserDirectoryApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_directory_get_domain_list**](UserDirectoryApi.md#user_directory_get_domain_list) | **GET** /UserDirectory/{moId}/domainList | List of Windows domains available for user searches, if the underlying system supports windows domain membership. 
[**user_directory_retrieve_user_groups**](UserDirectoryApi.md#user_directory_retrieve_user_groups) | **POST** /UserDirectory/{moId}/RetrieveUserGroups | Returns a list of *UserSearchResult* objects describing the users and groups defined for the server. 


# **user_directory_get_domain_list**
> List[str] user_directory_get_domain_list(mo_id)

List of Windows domains available for user searches, if the underlying system supports windows domain membership. 

List of Windows domains available for user searches, if the underlying system supports windows domain membership.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.UserDirectoryApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of Windows domains available for user searches, if the underlying system supports windows domain membership. 
        api_response = api_instance.user_directory_get_domain_list(mo_id)
        print("The response of UserDirectoryApi->user_directory_get_domain_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDirectoryApi->user_directory_get_domain_list: %s\n" % e)
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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_directory_retrieve_user_groups**
> List[UserSearchResult] user_directory_retrieve_user_groups(mo_id, retrieve_user_groups_request_type)

Returns a list of *UserSearchResult* objects describing the users and groups defined for the server. 

Returns a list of *UserSearchResult* objects describing the users and groups defined for the server. - On Windows, the search for users and groups is restricted to   the given domain. If you omit the domain argument, then   the search is performed on local users and groups. - On ESX Server (or Linux systems), the method returns the list   of users and groups that are specified in the /etc/passwd file.   If the password file contains Sun NIS or NIS+ users and groups,   the returned list includes information about those as well.    You must hold the Authorization.ModifyPermissions privilege to invoke this method. If you hold the privilege on any ManagedEntity, you will have access to user and group information for the server.  As of vSphere API 5.1: - Local user groups on ESXi are not supported and this method will   not return information about local groups on the ESXi host.   Information about Active Directory groups is not affected. - Some special system users on ESXi like 'nfsnobody' and 'daemon'   will be filtered out by this method. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_user_groups_request_type import RetrieveUserGroupsRequestType
from vmware_vi.models.user_search_result import UserSearchResult
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
    api_instance = vmware_vi.UserDirectoryApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_user_groups_request_type = vmware_vi.RetrieveUserGroupsRequestType() # RetrieveUserGroupsRequestType | 

    try:
        # Returns a list of *UserSearchResult* objects describing the users and groups defined for the server. 
        api_response = api_instance.user_directory_retrieve_user_groups(mo_id, retrieve_user_groups_request_type)
        print("The response of UserDirectoryApi->user_directory_retrieve_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDirectoryApi->user_directory_retrieve_user_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_user_groups_request_type** | [**RetrieveUserGroupsRequestType**](RetrieveUserGroupsRequestType.md)|  | 

### Return type

[**List[UserSearchResult]**](UserSearchResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotSupported***: If you specify a domain for systems that do not support domains, such as an ESX Server. The method also throws NotSupported if you specify membership (belongsToGroup or belongsToUser) and the server does not support by-membership queries.  ***NotFound***: If any of the domain, belongsToGroup, or belongsToUser arguments refer to entities that do not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

