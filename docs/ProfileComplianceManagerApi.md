# vmware_vi.ProfileComplianceManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_compliance_manager_check_compliance_task**](ProfileComplianceManagerApi.md#profile_compliance_manager_check_compliance_task) | **POST** /ProfileComplianceManager/{moId}/CheckCompliance_Task | Check compliance of an entity against a Profile. 
[**profile_compliance_manager_clear_compliance_status**](ProfileComplianceManagerApi.md#profile_compliance_manager_clear_compliance_status) | **POST** /ProfileComplianceManager/{moId}/ClearComplianceStatus | Clear the saved ComplianceResult based on profile and entity filtering criteria. 
[**profile_compliance_manager_query_compliance_status**](ProfileComplianceManagerApi.md#profile_compliance_manager_query_compliance_status) | **POST** /ProfileComplianceManager/{moId}/QueryComplianceStatus | Query the compliance status based on Profile and Entity filter. 
[**profile_compliance_manager_query_expression_metadata**](ProfileComplianceManagerApi.md#profile_compliance_manager_query_expression_metadata) | **POST** /ProfileComplianceManager/{moId}/QueryExpressionMetadata | Query the metadata for the expressions. 


# **profile_compliance_manager_check_compliance_task**
> ManagedObjectReference profile_compliance_manager_check_compliance_task(mo_id, check_compliance_request_type)

Check compliance of an entity against a Profile. 

Check compliance of an entity against a Profile.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_compliance_request_type import CheckComplianceRequestType
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
    api_instance = vmware_vi.ProfileComplianceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_compliance_request_type = vmware_vi.CheckComplianceRequestType() # CheckComplianceRequestType | 

    try:
        # Check compliance of an entity against a Profile. 
        api_response = api_instance.profile_compliance_manager_check_compliance_task(mo_id, check_compliance_request_type)
        print("The response of ProfileComplianceManagerApi->profile_compliance_manager_check_compliance_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileComplianceManagerApi->profile_compliance_manager_check_compliance_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_compliance_request_type** | [**CheckComplianceRequestType**](CheckComplianceRequestType.md)|  | 

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
**200** | Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_compliance_manager_clear_compliance_status**
> profile_compliance_manager_clear_compliance_status(mo_id, clear_compliance_status_request_type)

Clear the saved ComplianceResult based on profile and entity filtering criteria. 

Clear the saved ComplianceResult based on profile and entity filtering criteria.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Profile.Clear 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clear_compliance_status_request_type import ClearComplianceStatusRequestType
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
    api_instance = vmware_vi.ProfileComplianceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clear_compliance_status_request_type = vmware_vi.ClearComplianceStatusRequestType() # ClearComplianceStatusRequestType | 

    try:
        # Clear the saved ComplianceResult based on profile and entity filtering criteria. 
        api_instance.profile_compliance_manager_clear_compliance_status(mo_id, clear_compliance_status_request_type)
    except Exception as e:
        print("Exception when calling ProfileComplianceManagerApi->profile_compliance_manager_clear_compliance_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clear_compliance_status_request_type** | [**ClearComplianceStatusRequestType**](ClearComplianceStatusRequestType.md)|  | 

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

# **profile_compliance_manager_query_compliance_status**
> List[ComplianceResult] profile_compliance_manager_query_compliance_status(mo_id, query_compliance_status_request_type)

Query the compliance status based on Profile and Entity filter. 

Query the compliance status based on Profile and Entity filter.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.compliance_result import ComplianceResult
from vmware_vi.models.query_compliance_status_request_type import QueryComplianceStatusRequestType
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
    api_instance = vmware_vi.ProfileComplianceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_compliance_status_request_type = vmware_vi.QueryComplianceStatusRequestType() # QueryComplianceStatusRequestType | 

    try:
        # Query the compliance status based on Profile and Entity filter. 
        api_response = api_instance.profile_compliance_manager_query_compliance_status(mo_id, query_compliance_status_request_type)
        print("The response of ProfileComplianceManagerApi->profile_compliance_manager_query_compliance_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileComplianceManagerApi->profile_compliance_manager_query_compliance_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_compliance_status_request_type** | [**QueryComplianceStatusRequestType**](QueryComplianceStatusRequestType.md)|  | 

### Return type

[**List[ComplianceResult]**](ComplianceResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ComplianceResult. ComplianceResult information may not be available for all the entities. If the ComplianceResult is not available already, a new ComplianceCheck will not be triggered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_compliance_manager_query_expression_metadata**
> List[ProfileExpressionMetadata] profile_compliance_manager_query_expression_metadata(mo_id, query_expression_metadata_request_type)

Query the metadata for the expressions. 

Query the metadata for the expressions.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.profile_expression_metadata import ProfileExpressionMetadata
from vmware_vi.models.query_expression_metadata_request_type import QueryExpressionMetadataRequestType
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
    api_instance = vmware_vi.ProfileComplianceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_expression_metadata_request_type = vmware_vi.QueryExpressionMetadataRequestType() # QueryExpressionMetadataRequestType | 

    try:
        # Query the metadata for the expressions. 
        api_response = api_instance.profile_compliance_manager_query_expression_metadata(mo_id, query_expression_metadata_request_type)
        print("The response of ProfileComplianceManagerApi->profile_compliance_manager_query_expression_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileComplianceManagerApi->profile_compliance_manager_query_expression_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_expression_metadata_request_type** | [**QueryExpressionMetadataRequestType**](QueryExpressionMetadataRequestType.md)|  | 

### Return type

[**List[ProfileExpressionMetadata]**](ProfileExpressionMetadata.md)

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

