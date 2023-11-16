# vmware_vi.HostProfileManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_profile_manager_apply_entities_config_task**](HostProfileManagerApi.md#host_profile_manager_apply_entities_config_task) | **POST** /HostProfileManager/{moId}/ApplyEntitiesConfig_Task | The task for applying host configuration on a list of hosts. 
[**host_profile_manager_apply_host_config_task**](HostProfileManagerApi.md#host_profile_manager_apply_host_config_task) | **POST** /HostProfileManager/{moId}/ApplyHostConfig_Task | Apply the configuration to the host. 
[**host_profile_manager_check_answer_file_status_task**](HostProfileManagerApi.md#host_profile_manager_check_answer_file_status_task) | **POST** /HostProfileManager/{moId}/CheckAnswerFileStatus_Task | Check the validity of the answer files for the specified hosts. 
[**host_profile_manager_composite_host_profile_task**](HostProfileManagerApi.md#host_profile_manager_composite_host_profile_task) | **POST** /HostProfileManager/{moId}/CompositeHostProfile_Task | Composes (merge, replace, delete, disable) the selected configurations into the target host profiles. 
[**host_profile_manager_create_default_profile**](HostProfileManagerApi.md#host_profile_manager_create_default_profile) | **POST** /HostProfileManager/{moId}/CreateDefaultProfile | Create a default subprofile of a given type (for example, a *VirtualSwitchProfile*). 
[**host_profile_manager_create_profile**](HostProfileManagerApi.md#host_profile_manager_create_profile) | **POST** /HostProfileManager/{moId}/CreateProfile | Create a profile from the specified CreateSpec. 
[**host_profile_manager_export_answer_file_task**](HostProfileManagerApi.md#host_profile_manager_export_answer_file_task) | **POST** /HostProfileManager/{moId}/ExportAnswerFile_Task | Export a host&#39;s answer file into a serialized form. 
[**host_profile_manager_find_associated_profile**](HostProfileManagerApi.md#host_profile_manager_find_associated_profile) | **POST** /HostProfileManager/{moId}/FindAssociatedProfile | Get the profile(s) to which this entity is associated. 
[**host_profile_manager_generate_config_task_list**](HostProfileManagerApi.md#host_profile_manager_generate_config_task_list) | **POST** /HostProfileManager/{moId}/GenerateConfigTaskList | Generate a list of configuration tasks that will be performed on the host during HostProfile application. 
[**host_profile_manager_generate_host_config_task_spec_task**](HostProfileManagerApi.md#host_profile_manager_generate_host_config_task_spec_task) | **POST** /HostProfileManager/{moId}/GenerateHostConfigTaskSpec_Task | This method generates *ApplyHostProfileConfigurationSpec* data object for each host which can be passed as input to *HostProfileManager.ApplyEntitiesConfig_Task* to configure that host. 
[**host_profile_manager_generate_host_profile_task_list_task**](HostProfileManagerApi.md#host_profile_manager_generate_host_profile_task_list_task) | **POST** /HostProfileManager/{moId}/GenerateHostProfileTaskList_Task | Generate a list of configuration tasks that will be performed on the host during HostProfile application. 
[**host_profile_manager_get_profile**](HostProfileManagerApi.md#host_profile_manager_get_profile) | **GET** /HostProfileManager/{moId}/profile | A list of profiles known to this ProfileManager. 
[**host_profile_manager_query_answer_file_status**](HostProfileManagerApi.md#host_profile_manager_query_answer_file_status) | **POST** /HostProfileManager/{moId}/QueryAnswerFileStatus | Returns the status of the answer files associated with specified hosts. 
[**host_profile_manager_query_host_profile_metadata**](HostProfileManagerApi.md#host_profile_manager_query_host_profile_metadata) | **POST** /HostProfileManager/{moId}/QueryHostProfileMetadata | Retrieve the metadata for a set of profiles. 
[**host_profile_manager_query_policy_metadata**](HostProfileManagerApi.md#host_profile_manager_query_policy_metadata) | **POST** /HostProfileManager/{moId}/QueryPolicyMetadata | Get the Metadata information for the policyNames. 
[**host_profile_manager_query_profile_structure**](HostProfileManagerApi.md#host_profile_manager_query_profile_structure) | **POST** /HostProfileManager/{moId}/QueryProfileStructure | Get information about the structure of the profile. 
[**host_profile_manager_retrieve_answer_file**](HostProfileManagerApi.md#host_profile_manager_retrieve_answer_file) | **POST** /HostProfileManager/{moId}/RetrieveAnswerFile | Returns the answer file associated with a particular host. 
[**host_profile_manager_retrieve_answer_file_for_profile**](HostProfileManagerApi.md#host_profile_manager_retrieve_answer_file_for_profile) | **POST** /HostProfileManager/{moId}/RetrieveAnswerFileForProfile | Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile. 
[**host_profile_manager_retrieve_host_customizations**](HostProfileManagerApi.md#host_profile_manager_retrieve_host_customizations) | **POST** /HostProfileManager/{moId}/RetrieveHostCustomizations | This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFile. 
[**host_profile_manager_retrieve_host_customizations_for_profile**](HostProfileManagerApi.md#host_profile_manager_retrieve_host_customizations_for_profile) | **POST** /HostProfileManager/{moId}/RetrieveHostCustomizationsForProfile | This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFileForProfile. 
[**host_profile_manager_update_answer_file_task**](HostProfileManagerApi.md#host_profile_manager_update_answer_file_task) | **POST** /HostProfileManager/{moId}/UpdateAnswerFile_Task | Update the *AnswerFile* for the specified host. 
[**host_profile_manager_update_host_customizations_task**](HostProfileManagerApi.md#host_profile_manager_update_host_customizations_task) | **POST** /HostProfileManager/{moId}/UpdateHostCustomizations_Task | This is the batch version of vim.profile.host.ProfileManager@updateAnswerFile. 
[**host_profile_manager_validate_host_profile_composition_task**](HostProfileManagerApi.md#host_profile_manager_validate_host_profile_composition_task) | **POST** /HostProfileManager/{moId}/ValidateHostProfileComposition_Task | Validates the proposed host profile composition. 


# **host_profile_manager_apply_entities_config_task**
> ManagedObjectReference host_profile_manager_apply_entities_config_task(mo_id, apply_entities_config_request_type)

The task for applying host configuration on a list of hosts. 

The task for applying host configuration on a list of hosts.  This is the batch version of <code>applyHostConfiguration</code>. The implementation of this method will: When a host is in a DRS cluster but doesn't satisfy the state requirement such as that the host is not in the required maintenance mode, this method uses DRS feature to put the host into maintenance mode. This method will apply a host profile to a stateful host or stateless host; or apply a host profile to a stateless host by reboot. After a host is reboot, a check compliance is done to update the latest compliance status.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.apply_entities_config_request_type import ApplyEntitiesConfigRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    apply_entities_config_request_type = vmware_vi.ApplyEntitiesConfigRequestType() # ApplyEntitiesConfigRequestType | 

    try:
        # The task for applying host configuration on a list of hosts. 
        api_response = api_instance.host_profile_manager_apply_entities_config_task(mo_id, apply_entities_config_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_apply_entities_config_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_apply_entities_config_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **apply_entities_config_request_type** | [**ApplyEntitiesConfigRequestType**](ApplyEntitiesConfigRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. If the task is successful, the *Task*.*Task.info*.*TaskInfo.result* property is an array of *ApplyHostProfileConfigurationResult* objects. Each *ApplyHostProfileConfigurationResult* is for each host in the provided host list.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_apply_host_config_task**
> ManagedObjectReference host_profile_manager_apply_host_config_task(mo_id, apply_host_config_request_type)

Apply the configuration to the host. 

Apply the configuration to the host.  If you specify any user input, the configuration will be saved in the *AnswerFile* associated with the host. If there is no answer file, the Profile Engine will create one.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.apply_host_config_request_type import ApplyHostConfigRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    apply_host_config_request_type = vmware_vi.ApplyHostConfigRequestType() # ApplyHostConfigRequestType | 

    try:
        # Apply the configuration to the host. 
        api_response = api_instance.host_profile_manager_apply_host_config_task(mo_id, apply_host_config_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_apply_host_config_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_apply_host_config_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **apply_host_config_request_type** | [**ApplyHostConfigRequestType**](ApplyHostConfigRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: if the host is not in maintenance mode and the configuration specification requires it.  ***HostConfigFailed***: if the ESX Server cannot apply the configuration changes.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_check_answer_file_status_task**
> ManagedObjectReference host_profile_manager_check_answer_file_status_task(mo_id, check_answer_file_status_request_type)

Check the validity of the answer files for the specified hosts. 

Check the validity of the answer files for the specified hosts.  The Profile Engine uses the profile associated with a host to check the answer file.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_answer_file_status_request_type import CheckAnswerFileStatusRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_answer_file_status_request_type = vmware_vi.CheckAnswerFileStatusRequestType() # CheckAnswerFileStatusRequestType | 

    try:
        # Check the validity of the answer files for the specified hosts. 
        api_response = api_instance.host_profile_manager_check_answer_file_status_task(mo_id, check_answer_file_status_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_check_answer_file_status_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_check_answer_file_status_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_answer_file_status_request_type** | [**CheckAnswerFileStatusRequestType**](CheckAnswerFileStatusRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. If the task is successful, the *Task*.*Task.info*.*TaskInfo.result* property contains a list of *AnswerFileStatusResult* objects.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_composite_host_profile_task**
> ManagedObjectReference host_profile_manager_composite_host_profile_task(mo_id, composite_host_profile_request_type)

Composes (merge, replace, delete, disable) the selected configurations into the target host profiles. 

Composes (merge, replace, delete, disable) the selected configurations into the target host profiles.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.composite_host_profile_request_type import CompositeHostProfileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    composite_host_profile_request_type = vmware_vi.CompositeHostProfileRequestType() # CompositeHostProfileRequestType | 

    try:
        # Composes (merge, replace, delete, disable) the selected configurations into the target host profiles. 
        api_response = api_instance.host_profile_manager_composite_host_profile_task(mo_id, composite_host_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_composite_host_profile_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_composite_host_profile_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **composite_host_profile_request_type** | [**CompositeHostProfileRequestType**](CompositeHostProfileRequestType.md)|  | 

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
**200** | This method will returns a *Task* object with which to monitor the operation. The *Task*.*Task.info*.*TaskInfo.result* will contain a *HostProfileManagerCompositionResult* object containing the status of the operation, and details about any composition errors. The definitions of all the parameters are same as those in *HostProfileManager.ValidateHostProfileComposition_Task*.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_create_default_profile**
> ApplyProfile host_profile_manager_create_default_profile(mo_id, create_default_profile_request_type)

Create a default subprofile of a given type (for example, a *VirtualSwitchProfile*). 

Create a default subprofile of a given type (for example, a *VirtualSwitchProfile*).  After you create the subprofile, you can add it to a configuration specification and update the host profile: - Call the <code>CreateDefaultProfile</code> method. - Create a *HostProfileCompleteConfigSpec* object. - Copy the existing profile from the host configuration information   (*HostProfile*.*Profile.config*.*HostProfileConfigInfo.applyProfile*) to the configuration specification. - Add the new subprofile to the configuration specification. For example,   if you create a <code>VirtualSwitchProfile</code>, you would add it to the list   of virtual switches in the network profile for the configuration specification   (*NetworkProfile*.*NetworkProfile.vswitch*\\[\\]). - Call *HostProfile*.*HostProfile.UpdateHostProfile*   to save the new subprofile.      ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.apply_profile import ApplyProfile
from vmware_vi.models.create_default_profile_request_type import CreateDefaultProfileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_default_profile_request_type = vmware_vi.CreateDefaultProfileRequestType() # CreateDefaultProfileRequestType | 

    try:
        # Create a default subprofile of a given type (for example, a *VirtualSwitchProfile*). 
        api_response = api_instance.host_profile_manager_create_default_profile(mo_id, create_default_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_create_default_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_create_default_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_default_profile_request_type** | [**CreateDefaultProfileRequestType**](CreateDefaultProfileRequestType.md)|  | 

### Return type

[**ApplyProfile**](ApplyProfile.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Derived subprofile of type &lt;code&gt;profileType&lt;/code&gt;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_create_profile**
> ManagedObjectReference host_profile_manager_create_profile(mo_id, create_profile_request_type)

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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_profile_request_type = vmware_vi.CreateProfileRequestType() # CreateProfileRequestType | 

    try:
        # Create a profile from the specified CreateSpec. 
        api_response = api_instance.host_profile_manager_create_profile(mo_id, create_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_create_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_create_profile: %s\n" % e)
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

# **host_profile_manager_export_answer_file_task**
> ManagedObjectReference host_profile_manager_export_answer_file_task(mo_id, export_answer_file_request_type)

Export a host's answer file into a serialized form. 

Export a host's answer file into a serialized form.  The method returns a string that contains only the list of user input options. See *AnswerFile*.*AnswerFile.userInput*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Profile.Export 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.export_answer_file_request_type import ExportAnswerFileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    export_answer_file_request_type = vmware_vi.ExportAnswerFileRequestType() # ExportAnswerFileRequestType | 

    try:
        # Export a host's answer file into a serialized form. 
        api_response = api_instance.host_profile_manager_export_answer_file_task(mo_id, export_answer_file_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_export_answer_file_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_export_answer_file_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **export_answer_file_request_type** | [**ExportAnswerFileRequestType**](ExportAnswerFileRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. If the task is successful, the *Task*.*Task.info*.*TaskInfo.result* property is a string that contains a serialized form of the answer file.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_find_associated_profile**
> List[ManagedObjectReference] host_profile_manager_find_associated_profile(mo_id, find_associated_profile_request_type)

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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_associated_profile_request_type = vmware_vi.FindAssociatedProfileRequestType() # FindAssociatedProfileRequestType | 

    try:
        # Get the profile(s) to which this entity is associated. 
        api_response = api_instance.host_profile_manager_find_associated_profile(mo_id, find_associated_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_find_associated_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_find_associated_profile: %s\n" % e)
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

# **host_profile_manager_generate_config_task_list**
> HostProfileManagerConfigTaskList host_profile_manager_generate_config_task_list(mo_id, generate_config_task_list_request_type)

Generate a list of configuration tasks that will be performed on the host during HostProfile application. 

Deprecated as of vSphere API 6.0 use *HostProfileManager.GenerateHostProfileTaskList_Task*.  Generate a list of configuration tasks that will be performed on the host during HostProfile application.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_config_task_list_request_type import GenerateConfigTaskListRequestType
from vmware_vi.models.host_profile_manager_config_task_list import HostProfileManagerConfigTaskList
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_config_task_list_request_type = vmware_vi.GenerateConfigTaskListRequestType() # GenerateConfigTaskListRequestType | 

    try:
        # Generate a list of configuration tasks that will be performed on the host during HostProfile application. 
        api_response = api_instance.host_profile_manager_generate_config_task_list(mo_id, generate_config_task_list_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_generate_config_task_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_generate_config_task_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_config_task_list_request_type** | [**GenerateConfigTaskListRequestType**](GenerateConfigTaskListRequestType.md)|  | 

### Return type

[**HostProfileManagerConfigTaskList**](HostProfileManagerConfigTaskList.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Configuration tasks.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_generate_host_config_task_spec_task**
> ManagedObjectReference host_profile_manager_generate_host_config_task_spec_task(mo_id, generate_host_config_task_spec_request_type)

This method generates *ApplyHostProfileConfigurationSpec* data object for each host which can be passed as input to *HostProfileManager.ApplyEntitiesConfig_Task* to configure that host. 

This method generates *ApplyHostProfileConfigurationSpec* data object for each host which can be passed as input to *HostProfileManager.ApplyEntitiesConfig_Task* to configure that host.  For each host, this method goes through two stages, *HostProfile.ExecuteHostProfile* stage *HostProfileManager.GenerateHostProfileTaskList_Task* stage. If the *HostProfile.ExecuteHostProfile* stage completes successfully then the method invokes the *HostProfileManager.GenerateHostProfileTaskList_Task* stage to generate the list of configuration tasks that are needed to configure the host. This method will return a task to monitor the progress of the operation.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_host_config_task_spec_request_type import GenerateHostConfigTaskSpecRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_host_config_task_spec_request_type = vmware_vi.GenerateHostConfigTaskSpecRequestType() # GenerateHostConfigTaskSpecRequestType | 

    try:
        # This method generates *ApplyHostProfileConfigurationSpec* data object for each host which can be passed as input to *HostProfileManager.ApplyEntitiesConfig_Task* to configure that host. 
        api_response = api_instance.host_profile_manager_generate_host_config_task_spec_task(mo_id, generate_host_config_task_spec_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_generate_host_config_task_spec_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_generate_host_config_task_spec_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_host_config_task_spec_request_type** | [**GenerateHostConfigTaskSpecRequestType**](GenerateHostConfigTaskSpecRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. If the task is successful, the *Task*.*Task.info*.*TaskInfo.result* property is a *ApplyHostProfileConfigurationSpec* object.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_generate_host_profile_task_list_task**
> ManagedObjectReference host_profile_manager_generate_host_profile_task_list_task(mo_id, generate_host_profile_task_list_request_type)

Generate a list of configuration tasks that will be performed on the host during HostProfile application. 

Generate a list of configuration tasks that will be performed on the host during HostProfile application.  This differs from the *HostProfileManager.GenerateConfigTaskList* method in that it returns a task to monitor the progress of the operation.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_host_profile_task_list_request_type import GenerateHostProfileTaskListRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_host_profile_task_list_request_type = vmware_vi.GenerateHostProfileTaskListRequestType() # GenerateHostProfileTaskListRequestType | 

    try:
        # Generate a list of configuration tasks that will be performed on the host during HostProfile application. 
        api_response = api_instance.host_profile_manager_generate_host_profile_task_list_task(mo_id, generate_host_profile_task_list_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_generate_host_profile_task_list_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_generate_host_profile_task_list_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_host_profile_task_list_request_type** | [**GenerateHostProfileTaskListRequestType**](GenerateHostProfileTaskListRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. If the task is successful, the *Task*.*Task.info*.*TaskInfo.result* property is a *HostProfileManagerConfigTaskList* object.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_get_profile**
> List[ManagedObjectReference] host_profile_manager_get_profile(mo_id)

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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of profiles known to this ProfileManager. 
        api_response = api_instance.host_profile_manager_get_profile(mo_id)
        print("The response of HostProfileManagerApi->host_profile_manager_get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_get_profile: %s\n" % e)
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

# **host_profile_manager_query_answer_file_status**
> List[AnswerFileStatusResult] host_profile_manager_query_answer_file_status(mo_id, query_answer_file_status_request_type)

Returns the status of the answer files associated with specified hosts. 

Returns the status of the answer files associated with specified hosts.  This method returns the most recent status determined by *HostProfileManager.CheckAnswerFileStatus_Task*. See *HostProfileManagerAnswerFileStatus_enum* for valid values.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.answer_file_status_result import AnswerFileStatusResult
from vmware_vi.models.query_answer_file_status_request_type import QueryAnswerFileStatusRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_answer_file_status_request_type = vmware_vi.QueryAnswerFileStatusRequestType() # QueryAnswerFileStatusRequestType | 

    try:
        # Returns the status of the answer files associated with specified hosts. 
        api_response = api_instance.host_profile_manager_query_answer_file_status(mo_id, query_answer_file_status_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_query_answer_file_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_query_answer_file_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_answer_file_status_request_type** | [**QueryAnswerFileStatusRequestType**](QueryAnswerFileStatusRequestType.md)|  | 

### Return type

[**List[AnswerFileStatusResult]**](AnswerFileStatusResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of answer file status objects.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_query_host_profile_metadata**
> List[ProfileMetadata] host_profile_manager_query_host_profile_metadata(mo_id, query_host_profile_metadata_request_type)

Retrieve the metadata for a set of profiles. 

Retrieve the metadata for a set of profiles.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_metadata import ProfileMetadata
from vmware_vi.models.query_host_profile_metadata_request_type import QueryHostProfileMetadataRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_host_profile_metadata_request_type = vmware_vi.QueryHostProfileMetadataRequestType() # QueryHostProfileMetadataRequestType | 

    try:
        # Retrieve the metadata for a set of profiles. 
        api_response = api_instance.host_profile_manager_query_host_profile_metadata(mo_id, query_host_profile_metadata_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_query_host_profile_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_query_host_profile_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_host_profile_metadata_request_type** | [**QueryHostProfileMetadataRequestType**](QueryHostProfileMetadataRequestType.md)|  | 

### Return type

[**List[ProfileMetadata]**](ProfileMetadata.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of profile metadata objects.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_query_policy_metadata**
> List[ProfilePolicyMetadata] host_profile_manager_query_policy_metadata(mo_id, query_policy_metadata_request_type)

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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_policy_metadata_request_type = vmware_vi.QueryPolicyMetadataRequestType() # QueryPolicyMetadataRequestType | 

    try:
        # Get the Metadata information for the policyNames. 
        api_response = api_instance.host_profile_manager_query_policy_metadata(mo_id, query_policy_metadata_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_query_policy_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_query_policy_metadata: %s\n" % e)
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

# **host_profile_manager_query_profile_structure**
> ProfileProfileStructure host_profile_manager_query_profile_structure(mo_id, query_profile_structure_request_type)

Get information about the structure of the profile. 

Get information about the structure of the profile.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_profile_structure import ProfileProfileStructure
from vmware_vi.models.query_profile_structure_request_type import QueryProfileStructureRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_profile_structure_request_type = vmware_vi.QueryProfileStructureRequestType() # QueryProfileStructureRequestType | 

    try:
        # Get information about the structure of the profile. 
        api_response = api_instance.host_profile_manager_query_profile_structure(mo_id, query_profile_structure_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_query_profile_structure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_query_profile_structure: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_profile_structure_request_type** | [**QueryProfileStructureRequestType**](QueryProfileStructureRequestType.md)|  | 

### Return type

[**ProfileProfileStructure**](ProfileProfileStructure.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile structure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_retrieve_answer_file**
> AnswerFile host_profile_manager_retrieve_answer_file(mo_id, retrieve_answer_file_request_type)

Returns the answer file associated with a particular host. 

Returns the answer file associated with a particular host.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.answer_file import AnswerFile
from vmware_vi.models.retrieve_answer_file_request_type import RetrieveAnswerFileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_answer_file_request_type = vmware_vi.RetrieveAnswerFileRequestType() # RetrieveAnswerFileRequestType | 

    try:
        # Returns the answer file associated with a particular host. 
        api_response = api_instance.host_profile_manager_retrieve_answer_file(mo_id, retrieve_answer_file_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_retrieve_answer_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_retrieve_answer_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_answer_file_request_type** | [**RetrieveAnswerFileRequestType**](RetrieveAnswerFileRequestType.md)|  | 

### Return type

[**AnswerFile**](AnswerFile.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Answer file object will be returned if it exists.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_retrieve_answer_file_for_profile**
> AnswerFile host_profile_manager_retrieve_answer_file_for_profile(mo_id, retrieve_answer_file_for_profile_request_type)

Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile. 

Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.answer_file import AnswerFile
from vmware_vi.models.retrieve_answer_file_for_profile_request_type import RetrieveAnswerFileForProfileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_answer_file_for_profile_request_type = vmware_vi.RetrieveAnswerFileForProfileRequestType() # RetrieveAnswerFileForProfileRequestType | 

    try:
        # Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile. 
        api_response = api_instance.host_profile_manager_retrieve_answer_file_for_profile(mo_id, retrieve_answer_file_for_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_retrieve_answer_file_for_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_retrieve_answer_file_for_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_answer_file_for_profile_request_type** | [**RetrieveAnswerFileForProfileRequestType**](RetrieveAnswerFileForProfileRequestType.md)|  | 

### Return type

[**AnswerFile**](AnswerFile.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Answer file object will be returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_retrieve_host_customizations**
> List[StructuredCustomizations] host_profile_manager_retrieve_host_customizations(mo_id, retrieve_host_customizations_request_type)

This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFile. 

This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFile.  Returns a map that contains the hosts and their answer file data objects.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_host_customizations_request_type import RetrieveHostCustomizationsRequestType
from vmware_vi.models.structured_customizations import StructuredCustomizations
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_host_customizations_request_type = vmware_vi.RetrieveHostCustomizationsRequestType() # RetrieveHostCustomizationsRequestType | 

    try:
        # This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFile. 
        api_response = api_instance.host_profile_manager_retrieve_host_customizations(mo_id, retrieve_host_customizations_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_retrieve_host_customizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_retrieve_host_customizations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_host_customizations_request_type** | [**RetrieveHostCustomizationsRequestType**](RetrieveHostCustomizationsRequestType.md)|  | 

### Return type

[**List[StructuredCustomizations]**](StructuredCustomizations.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map that contains the hosts and their answer files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_retrieve_host_customizations_for_profile**
> List[StructuredCustomizations] host_profile_manager_retrieve_host_customizations_for_profile(mo_id, retrieve_host_customizations_for_profile_request_type)

This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFileForProfile. 

This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFileForProfile.  Returns a map that contains the hosts and their answer files associated with these hosts, augmented with whatever answer file values are required for the supplied host profile.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_host_customizations_for_profile_request_type import RetrieveHostCustomizationsForProfileRequestType
from vmware_vi.models.structured_customizations import StructuredCustomizations
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_host_customizations_for_profile_request_type = vmware_vi.RetrieveHostCustomizationsForProfileRequestType() # RetrieveHostCustomizationsForProfileRequestType | 

    try:
        # This is the batch version of vim.profile.host.ProfileManager@retrieveAnswerFileForProfile. 
        api_response = api_instance.host_profile_manager_retrieve_host_customizations_for_profile(mo_id, retrieve_host_customizations_for_profile_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_retrieve_host_customizations_for_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_retrieve_host_customizations_for_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_host_customizations_for_profile_request_type** | [**RetrieveHostCustomizationsForProfileRequestType**](RetrieveHostCustomizationsForProfileRequestType.md)|  | 

### Return type

[**List[StructuredCustomizations]**](StructuredCustomizations.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map contains the hosts and their answer files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_update_answer_file_task**
> ManagedObjectReference host_profile_manager_update_answer_file_task(mo_id, update_answer_file_request_type)

Update the *AnswerFile* for the specified host. 

Update the *AnswerFile* for the specified host.  If there is no answer file associated with the host, the Profile Engine uses the answer file configuration specification to create a new one.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_answer_file_request_type import UpdateAnswerFileRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_answer_file_request_type = vmware_vi.UpdateAnswerFileRequestType() # UpdateAnswerFileRequestType | 

    try:
        # Update the *AnswerFile* for the specified host. 
        api_response = api_instance.host_profile_manager_update_answer_file_task(mo_id, update_answer_file_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_update_answer_file_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_update_answer_file_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_answer_file_request_type** | [**UpdateAnswerFileRequestType**](UpdateAnswerFileRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***AnswerFileUpdateFailed***: If the answer file could not be updated.  ***InvalidArgument***: If the input parameters are incorrect.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_update_host_customizations_task**
> ManagedObjectReference host_profile_manager_update_host_customizations_task(mo_id, update_host_customizations_request_type)

This is the batch version of vim.profile.host.ProfileManager@updateAnswerFile. 

This is the batch version of vim.profile.host.ProfileManager@updateAnswerFile.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_host_customizations_request_type import UpdateHostCustomizationsRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_host_customizations_request_type = vmware_vi.UpdateHostCustomizationsRequestType() # UpdateHostCustomizationsRequestType | 

    try:
        # This is the batch version of vim.profile.host.ProfileManager@updateAnswerFile. 
        api_response = api_instance.host_profile_manager_update_host_customizations_task(mo_id, update_host_customizations_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_update_host_customizations_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_update_host_customizations_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_host_customizations_request_type** | [**UpdateHostCustomizationsRequestType**](UpdateHostCustomizationsRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation with a result of *AnswerFileValidationResultMap* array.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_manager_validate_host_profile_composition_task**
> ManagedObjectReference host_profile_manager_validate_host_profile_composition_task(mo_id, validate_host_profile_composition_request_type)

Validates the proposed host profile composition. 

Validates the proposed host profile composition.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.validate_host_profile_composition_request_type import ValidateHostProfileCompositionRequestType
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
    api_instance = vmware_vi.HostProfileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    validate_host_profile_composition_request_type = vmware_vi.ValidateHostProfileCompositionRequestType() # ValidateHostProfileCompositionRequestType | 

    try:
        # Validates the proposed host profile composition. 
        api_response = api_instance.host_profile_manager_validate_host_profile_composition_task(mo_id, validate_host_profile_composition_request_type)
        print("The response of HostProfileManagerApi->host_profile_manager_validate_host_profile_composition_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileManagerApi->host_profile_manager_validate_host_profile_composition_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **validate_host_profile_composition_request_type** | [**ValidateHostProfileCompositionRequestType**](ValidateHostProfileCompositionRequestType.md)|  | 

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
**200** | This method will returns a *Task* object with which to monitor the operation. The *Task*.*Task.info*.*TaskInfo.result* will contain a *HostProfileManagerCompositionValidationResult* object containing the status of the operation, any validation errors and the validation results.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

