# vmware_vi.HostProfileApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_profile_associate_profile**](HostProfileApi.md#host_profile_associate_profile) | **POST** /HostProfile/{moId}/AssociateProfile | Associate a profile with a managed entity. 
[**host_profile_check_profile_compliance_task**](HostProfileApi.md#host_profile_check_profile_compliance_task) | **POST** /HostProfile/{moId}/CheckProfileCompliance_Task | Check compliance of an entity against a Profile. 
[**host_profile_destroy_profile**](HostProfileApi.md#host_profile_destroy_profile) | **POST** /HostProfile/{moId}/DestroyProfile | Destroy the profile. 
[**host_profile_dissociate_profile**](HostProfileApi.md#host_profile_dissociate_profile) | **POST** /HostProfile/{moId}/DissociateProfile | Remove the association between a profile and a managed entity. 
[**host_profile_execute_host_profile**](HostProfileApi.md#host_profile_execute_host_profile) | **POST** /HostProfile/{moId}/ExecuteHostProfile | Run the Profile Engine to determine the list of configuration changes needed for the specified host. 
[**host_profile_export_profile**](HostProfileApi.md#host_profile_export_profile) | **POST** /HostProfile/{moId}/ExportProfile | Export the profile in a serialized form. 
[**host_profile_get_compliance_check_time**](HostProfileApi.md#host_profile_get_compliance_check_time) | **GET** /HostProfile/{moId}/complianceCheckTime | The latest compliance check time. 
[**host_profile_get_compliance_status**](HostProfileApi.md#host_profile_get_compliance_status) | **GET** /HostProfile/{moId}/complianceStatus | Overall compliance of entities associated with this profile. 
[**host_profile_get_config**](HostProfileApi.md#host_profile_get_config) | **GET** /HostProfile/{moId}/config | Configuration data for the profile. 
[**host_profile_get_created_time**](HostProfileApi.md#host_profile_get_created_time) | **GET** /HostProfile/{moId}/createdTime | Time at which the profile was created. 
[**host_profile_get_description**](HostProfileApi.md#host_profile_get_description) | **GET** /HostProfile/{moId}/description | Localizable description of the profile 
[**host_profile_get_entity**](HostProfileApi.md#host_profile_get_entity) | **GET** /HostProfile/{moId}/entity | List of managed entities associated with the profile. 
[**host_profile_get_modified_time**](HostProfileApi.md#host_profile_get_modified_time) | **GET** /HostProfile/{moId}/modifiedTime | Time at which the profile was last modified. 
[**host_profile_get_name**](HostProfileApi.md#host_profile_get_name) | **GET** /HostProfile/{moId}/name | Name of the profile. 
[**host_profile_get_reference_host**](HostProfileApi.md#host_profile_get_reference_host) | **GET** /HostProfile/{moId}/referenceHost | Reference host in use for this host profile. 
[**host_profile_get_validation_failure_info**](HostProfileApi.md#host_profile_get_validation_failure_info) | **GET** /HostProfile/{moId}/validationFailureInfo | This object is created or updated if the *HostProfileValidationState_enum* is Failed. 
[**host_profile_get_validation_state**](HostProfileApi.md#host_profile_get_validation_state) | **GET** /HostProfile/{moId}/validationState | State of the host profile validation operation. 
[**host_profile_get_validation_state_update_time**](HostProfileApi.md#host_profile_get_validation_state_update_time) | **GET** /HostProfile/{moId}/validationStateUpdateTime | Update time of the validation operation. 
[**host_profile_host_profile_reset_validation_state**](HostProfileApi.md#host_profile_host_profile_reset_validation_state) | **POST** /HostProfile/{moId}/HostProfileResetValidationState | This API will update the validationState to Ready from Failed, invalidate the validationFailureInfo and reset the validationStateUpdateTime. 
[**host_profile_retrieve_description**](HostProfileApi.md#host_profile_retrieve_description) | **POST** /HostProfile/{moId}/RetrieveDescription | Returns the localizable description for the profile. 
[**host_profile_update_host_profile**](HostProfileApi.md#host_profile_update_host_profile) | **POST** /HostProfile/{moId}/UpdateHostProfile | Update the &lt;code&gt;HostProfile&lt;/code&gt; with the specified configuration data. 
[**host_profile_update_reference_host**](HostProfileApi.md#host_profile_update_reference_host) | **POST** /HostProfile/{moId}/UpdateReferenceHost | Sets the *HostProfile*.*HostProfile.referenceHost* property. 


# **host_profile_associate_profile**
> host_profile_associate_profile(mo_id, associate_profile_request_type)

Associate a profile with a managed entity. 

Associate a profile with a managed entity.  You can check the compliance of entities associated with a profile by calling the *Profile.CheckProfileCompliance_Task* method.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.associate_profile_request_type import AssociateProfileRequestType
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    associate_profile_request_type = vmware_vi.AssociateProfileRequestType() # AssociateProfileRequestType | 

    try:
        # Associate a profile with a managed entity. 
        api_instance.host_profile_associate_profile(mo_id, associate_profile_request_type)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_associate_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **associate_profile_request_type** | [**AssociateProfileRequestType**](AssociateProfileRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_check_profile_compliance_task**
> ManagedObjectReference host_profile_check_profile_compliance_task(mo_id, check_profile_compliance_request_type)

Check compliance of an entity against a Profile. 

Check compliance of an entity against a Profile.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_profile_compliance_request_type import CheckProfileComplianceRequestType
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_profile_compliance_request_type = vmware_vi.CheckProfileComplianceRequestType() # CheckProfileComplianceRequestType | 

    try:
        # Check compliance of an entity against a Profile. 
        api_response = api_instance.host_profile_check_profile_compliance_task(mo_id, check_profile_compliance_request_type)
        print("The response of HostProfileApi->host_profile_check_profile_compliance_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_check_profile_compliance_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_profile_compliance_request_type** | [**CheckProfileComplianceRequestType**](CheckProfileComplianceRequestType.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_destroy_profile**
> host_profile_destroy_profile(mo_id)

Destroy the profile. 

Destroy the profile.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Delete 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroy the profile. 
        api_instance.host_profile_destroy_profile(mo_id)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_destroy_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_dissociate_profile**
> host_profile_dissociate_profile(mo_id, dissociate_profile_request_type)

Remove the association between a profile and a managed entity. 

Remove the association between a profile and a managed entity.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dissociate_profile_request_type import DissociateProfileRequestType
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dissociate_profile_request_type = vmware_vi.DissociateProfileRequestType() # DissociateProfileRequestType | 

    try:
        # Remove the association between a profile and a managed entity. 
        api_instance.host_profile_dissociate_profile(mo_id, dissociate_profile_request_type)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_dissociate_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dissociate_profile_request_type** | [**DissociateProfileRequestType**](DissociateProfileRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_execute_host_profile**
> ProfileExecuteResult host_profile_execute_host_profile(mo_id, execute_host_profile_request_type)

Run the Profile Engine to determine the list of configuration changes needed for the specified host. 

Run the Profile Engine to determine the list of configuration changes needed for the specified host.  The method generates configuration changes based on the host profile.  You can also specify deferred parameters to verify additional host-specific data. The Profile Engine uses the policy options (*HostProfile*.*Profile.config*.*HostProfileConfigInfo.applyProfile*.*ApplyProfile.policy*\\[\\]) to determine the required parameters (*PolicyOption*.*PolicyOption.parameter*\\[\\]) for host configuration. If you do not provide all of the required parameters, you must call the method again to provide the complete list to the Profile Engine. After successful profile execution, when you apply the profile, the Profile Engine will save the host-specific data in an *AnswerFile*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.execute_host_profile_request_type import ExecuteHostProfileRequestType
from vmware_vi.models.profile_execute_result import ProfileExecuteResult
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    execute_host_profile_request_type = vmware_vi.ExecuteHostProfileRequestType() # ExecuteHostProfileRequestType | 

    try:
        # Run the Profile Engine to determine the list of configuration changes needed for the specified host. 
        api_response = api_instance.host_profile_execute_host_profile(mo_id, execute_host_profile_request_type)
        print("The response of HostProfileApi->host_profile_execute_host_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_execute_host_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **execute_host_profile_request_type** | [**ExecuteHostProfileRequestType**](ExecuteHostProfileRequestType.md)|  | 

### Return type

[**ProfileExecuteResult**](ProfileExecuteResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the execution. If the operation is successful (*ProfileExecuteResult*.*ProfileExecuteResult.status*&lt;code&gt;&#x3D;success&lt;/code&gt;), the result object includes a valid host configuration specification that you can pass to the *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task* method.  If the operation is not successful, the object contains error information or information about additional data required for the host configuration. If additional data is required, the required input list (*ProfileExecuteResult*.*ProfileExecuteResult.requireInput*\\[\\]) contains both the &lt;code&gt;deferredParam&lt;/code&gt; data and paths to missing parameters. After you fill in the missing parameters, pass the complete required input list via the &lt;code&gt;deferredParam&lt;/code&gt; parameter in another call to the execute method to finish input verification. After successful profile execution, you can pass the verified required input list to the *HostProfileManager.ApplyHostConfig_Task* method.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_export_profile**
> str host_profile_export_profile(mo_id)

Export the profile in a serialized form. 

Export the profile in a serialized form.  To use the serialized string to create a profile, specify a *ProfileSerializedCreateSpec* when you call the *HostProfileManager*.*ProfileManager.CreateProfile* method.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Export 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Export the profile in a serialized form. 
        api_response = api_instance.host_profile_export_profile(mo_id)
        print("The response of HostProfileApi->host_profile_export_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_export_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Serialized form of the profile.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_get_compliance_check_time**
> datetime host_profile_get_compliance_check_time(mo_id)

The latest compliance check time. 

The latest compliance check time. 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The latest compliance check time. 
        api_response = api_instance.host_profile_get_compliance_check_time(mo_id)
        print("The response of HostProfileApi->host_profile_get_compliance_check_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_compliance_check_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

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

# **host_profile_get_compliance_status**
> str host_profile_get_compliance_status(mo_id)

Overall compliance of entities associated with this profile. 

Overall compliance of entities associated with this profile.  If one of the entities is out of compliance, the profile is <code>nonCompliant</code>. If all entities are in compliance, the profile is <code>compliant</code>. If the compliance status of one of the entities is not known, compliance status of the profile is <code>unknown</code>. See *ComplianceResultStatus_enum*.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Overall compliance of entities associated with this profile. 
        api_response = api_instance.host_profile_get_compliance_status(mo_id)
        print("The response of HostProfileApi->host_profile_get_compliance_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_compliance_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **host_profile_get_config**
> ProfileConfigInfo host_profile_get_config(mo_id)

Configuration data for the profile. 

Configuration data for the profile.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_config_info import ProfileConfigInfo
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration data for the profile. 
        api_response = api_instance.host_profile_get_config(mo_id)
        print("The response of HostProfileApi->host_profile_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ProfileConfigInfo**](ProfileConfigInfo.md)

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

# **host_profile_get_created_time**
> datetime host_profile_get_created_time(mo_id)

Time at which the profile was created. 

Time at which the profile was created.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Time at which the profile was created. 
        api_response = api_instance.host_profile_get_created_time(mo_id)
        print("The response of HostProfileApi->host_profile_get_created_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_created_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

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

# **host_profile_get_description**
> ProfileDescription host_profile_get_description(mo_id)

Localizable description of the profile 

Deprecated as of vSphere API 5.0. use *Profile.RetrieveDescription* instead.  Localizable description of the profile  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_description import ProfileDescription
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Localizable description of the profile 
        api_response = api_instance.host_profile_get_description(mo_id)
        print("The response of HostProfileApi->host_profile_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ProfileDescription**](ProfileDescription.md)

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

# **host_profile_get_entity**
> List[ManagedObjectReference] host_profile_get_entity(mo_id)

List of managed entities associated with the profile. 

List of managed entities associated with the profile.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of managed entities associated with the profile. 
        api_response = api_instance.host_profile_get_entity(mo_id)
        print("The response of HostProfileApi->host_profile_get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_entity: %s\n" % e)
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
**200** | Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_get_modified_time**
> datetime host_profile_get_modified_time(mo_id)

Time at which the profile was last modified. 

Time at which the profile was last modified.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Time at which the profile was last modified. 
        api_response = api_instance.host_profile_get_modified_time(mo_id)
        print("The response of HostProfileApi->host_profile_get_modified_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_modified_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

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

# **host_profile_get_name**
> str host_profile_get_name(mo_id)

Name of the profile. 

Name of the profile.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of the profile. 
        api_response = api_instance.host_profile_get_name(mo_id)
        print("The response of HostProfileApi->host_profile_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **host_profile_get_reference_host**
> ManagedObjectReference host_profile_get_reference_host(mo_id)

Reference host in use for this host profile. 

Reference host in use for this host profile.  To set this property, use the *HostProfile.UpdateReferenceHost* method. If you do not specify a host for validation (*HostProfileCompleteConfigSpec*.*HostProfileCompleteConfigSpec.validatorHost*), the Profile Engine uses the reference host to validate the profile.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reference host in use for this host profile. 
        api_response = api_instance.host_profile_get_reference_host(mo_id)
        print("The response of HostProfileApi->host_profile_get_reference_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_reference_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_get_validation_failure_info**
> HostProfileValidationFailureInfo host_profile_get_validation_failure_info(mo_id)

This object is created or updated if the *HostProfileValidationState_enum* is Failed. 

This object is created or updated if the *HostProfileValidationState_enum* is Failed.  This object captures the most recent validation result for the host profile object in case of failure.  ***Since:*** vSphere API 6.7 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_profile_validation_failure_info import HostProfileValidationFailureInfo
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This object is created or updated if the *HostProfileValidationState_enum* is Failed. 
        api_response = api_instance.host_profile_get_validation_failure_info(mo_id)
        print("The response of HostProfileApi->host_profile_get_validation_failure_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_validation_failure_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostProfileValidationFailureInfo**](HostProfileValidationFailureInfo.md)

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

# **host_profile_get_validation_state**
> str host_profile_get_validation_state(mo_id)

State of the host profile validation operation. 

State of the host profile validation operation.  The values of the state will be one of *HostProfileValidationState_enum* enumerations.  ***Since:*** vSphere API 6.7 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # State of the host profile validation operation. 
        api_response = api_instance.host_profile_get_validation_state(mo_id)
        print("The response of HostProfileApi->host_profile_get_validation_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_validation_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **host_profile_get_validation_state_update_time**
> datetime host_profile_get_validation_state_update_time(mo_id)

Update time of the validation operation. 

Update time of the validation operation.  ***Since:*** vSphere API 6.7 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Update time of the validation operation. 
        api_response = api_instance.host_profile_get_validation_state_update_time(mo_id)
        print("The response of HostProfileApi->host_profile_get_validation_state_update_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_get_validation_state_update_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

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

# **host_profile_host_profile_reset_validation_state**
> host_profile_host_profile_reset_validation_state(mo_id)

This API will update the validationState to Ready from Failed, invalidate the validationFailureInfo and reset the validationStateUpdateTime. 

This API will update the validationState to Ready from Failed, invalidate the validationFailureInfo and reset the validationStateUpdateTime.  This API will return error if the validationState is Running.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Profile.Edit 

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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This API will update the validationState to Ready from Failed, invalidate the validationFailureInfo and reset the validationStateUpdateTime. 
        api_instance.host_profile_host_profile_reset_validation_state(mo_id)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_host_profile_reset_validation_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_retrieve_description**
> ProfileDescription host_profile_retrieve_description(mo_id)

Returns the localizable description for the profile. 

Returns the localizable description for the profile.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_description import ProfileDescription
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns the localizable description for the profile. 
        api_response = api_instance.host_profile_retrieve_description(mo_id)
        print("The response of HostProfileApi->host_profile_retrieve_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_retrieve_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ProfileDescription**](ProfileDescription.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile divided into sections containing element descriptions and messages.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_update_host_profile**
> host_profile_update_host_profile(mo_id, update_host_profile_request_type)

Update the <code>HostProfile</code> with the specified configuration data. 

Update the <code>HostProfile</code> with the specified configuration data.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_host_profile_request_type import UpdateHostProfileRequestType
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_host_profile_request_type = vmware_vi.UpdateHostProfileRequestType() # UpdateHostProfileRequestType | 

    try:
        # Update the <code>HostProfile</code> with the specified configuration data. 
        api_instance.host_profile_update_host_profile(mo_id, update_host_profile_request_type)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_update_host_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_host_profile_request_type** | [**UpdateHostProfileRequestType**](UpdateHostProfileRequestType.md)|  | 

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
**500** | ***DuplicateName***: If the profile with the new name already exists.  ***ProfileUpdateFailed***: if errors were encountered when updating the profile.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_profile_update_reference_host**
> host_profile_update_reference_host(mo_id, update_reference_host_request_type)

Sets the *HostProfile*.*HostProfile.referenceHost* property. 

Sets the *HostProfile*.*HostProfile.referenceHost* property.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_reference_host_request_type import UpdateReferenceHostRequestType
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
    api_instance = vmware_vi.HostProfileApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_reference_host_request_type = vmware_vi.UpdateReferenceHostRequestType() # UpdateReferenceHostRequestType | 

    try:
        # Sets the *HostProfile*.*HostProfile.referenceHost* property. 
        api_instance.host_profile_update_reference_host(mo_id, update_reference_host_request_type)
    except Exception as e:
        print("Exception when calling HostProfileApi->host_profile_update_reference_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_reference_host_request_type** | [**UpdateReferenceHostRequestType**](UpdateReferenceHostRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

