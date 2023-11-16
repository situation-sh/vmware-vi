# vmware_vi.ClusterProfileManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_profile_manager_create_profile**](ClusterProfileManagerApi.md#cluster_profile_manager_create_profile) | **POST** /ClusterProfileManager/{moId}/CreateProfile | Create a profile from the specified CreateSpec. 
[**cluster_profile_manager_find_associated_profile**](ClusterProfileManagerApi.md#cluster_profile_manager_find_associated_profile) | **POST** /ClusterProfileManager/{moId}/FindAssociatedProfile | Get the profile(s) to which this entity is associated. 
[**cluster_profile_manager_get_profile**](ClusterProfileManagerApi.md#cluster_profile_manager_get_profile) | **GET** /ClusterProfileManager/{moId}/profile | A list of profiles known to this ProfileManager. 
[**cluster_profile_manager_query_policy_metadata**](ClusterProfileManagerApi.md#cluster_profile_manager_query_policy_metadata) | **POST** /ClusterProfileManager/{moId}/QueryPolicyMetadata | Get the Metadata information for the policyNames. 


# **cluster_profile_manager_create_profile**
> ManagedObjectReference cluster_profile_manager_create_profile(mo_id, create_profile_request_type)

Create a profile from the specified CreateSpec. 

Create a profile from the specified CreateSpec.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_profile_request_type import CreateProfileRequestType
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
    api_instance = vmware_vi.ClusterProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_profile_request_type = vmware_vi.CreateProfileRequestType() # CreateProfileRequestType | 

    try:
        # Create a profile from the specified CreateSpec. 
        api_response = api_instance.cluster_profile_manager_create_profile(mo_id, create_profile_request_type)
        print("The response of ClusterProfileManagerApi->cluster_profile_manager_create_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterProfileManagerApi->cluster_profile_manager_create_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_profile_request_type** | [**CreateProfileRequestType**](CreateProfileRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile created from the specified createSpec.  Refers instance of *Profile*.  |  -  |
**500** | ***DuplicateName***: If a profile with the specified name already exists.  ***InvalidProfileReferenceHost***: if the specified reference host is incompatible or no reference host has been specified.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_profile_manager_find_associated_profile**
> List[ManagedObjectReference] cluster_profile_manager_find_associated_profile(mo_id, find_associated_profile_request_type)

Get the profile(s) to which this entity is associated. 

Get the profile(s) to which this entity is associated.  The list of profiles will only include profiles known to this profileManager.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_associated_profile_request_type import FindAssociatedProfileRequestType
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
    api_instance = vmware_vi.ClusterProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_associated_profile_request_type = vmware_vi.FindAssociatedProfileRequestType() # FindAssociatedProfileRequestType | 

    try:
        # Get the profile(s) to which this entity is associated. 
        api_response = api_instance.cluster_profile_manager_find_associated_profile(mo_id, find_associated_profile_request_type)
        print("The response of ClusterProfileManagerApi->cluster_profile_manager_find_associated_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterProfileManagerApi->cluster_profile_manager_find_associated_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_associated_profile_request_type** | [**FindAssociatedProfileRequestType**](FindAssociatedProfileRequestType.md)|  | 

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
**200** | Refers instances of *Profile*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_profile_manager_get_profile**
> List[ManagedObjectReference] cluster_profile_manager_get_profile(mo_id)

A list of profiles known to this ProfileManager. 

A list of profiles known to this ProfileManager.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.View 

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
    api_instance = vmware_vi.ClusterProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of profiles known to this ProfileManager. 
        api_response = api_instance.cluster_profile_manager_get_profile(mo_id)
        print("The response of ClusterProfileManagerApi->cluster_profile_manager_get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterProfileManagerApi->cluster_profile_manager_get_profile: %s\n" % e)
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
**200** | Refers instances of *Profile*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_profile_manager_query_policy_metadata**
> List[ProfilePolicyMetadata] cluster_profile_manager_query_policy_metadata(mo_id, query_policy_metadata_request_type)

Get the Metadata information for the policyNames. 

Get the Metadata information for the policyNames.  PolicyNames are available with the defaultProfile obtained by invoking the method createDefaultProfile.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_policy_metadata import ProfilePolicyMetadata
from vmware_vi.models.query_policy_metadata_request_type import QueryPolicyMetadataRequestType
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
    api_instance = vmware_vi.ClusterProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_policy_metadata_request_type = vmware_vi.QueryPolicyMetadataRequestType() # QueryPolicyMetadataRequestType | 

    try:
        # Get the Metadata information for the policyNames. 
        api_response = api_instance.cluster_profile_manager_query_policy_metadata(mo_id, query_policy_metadata_request_type)
        print("The response of ClusterProfileManagerApi->cluster_profile_manager_query_policy_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterProfileManagerApi->cluster_profile_manager_query_policy_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_policy_metadata_request_type** | [**QueryPolicyMetadataRequestType**](QueryPolicyMetadataRequestType.md)|  | 

### Return type

[**List[ProfilePolicyMetadata]**](ProfilePolicyMetadata.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata information for the policy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

