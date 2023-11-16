# vmware_vi.LicenseAssignmentManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_assignment_manager_query_assigned_licenses**](LicenseAssignmentManagerApi.md#license_assignment_manager_query_assigned_licenses) | **POST** /LicenseAssignmentManager/{moId}/QueryAssignedLicenses | Get information about all the licenses associated with an entity 
[**license_assignment_manager_remove_assigned_license**](LicenseAssignmentManagerApi.md#license_assignment_manager_remove_assigned_license) | **POST** /LicenseAssignmentManager/{moId}/RemoveAssignedLicense | Remove licenses associated with an entity 
[**license_assignment_manager_update_assigned_license**](LicenseAssignmentManagerApi.md#license_assignment_manager_update_assigned_license) | **POST** /LicenseAssignmentManager/{moId}/UpdateAssignedLicense | Update the license associated with an entity 


# **license_assignment_manager_query_assigned_licenses**
> List[LicenseAssignmentManagerLicenseAssignment] license_assignment_manager_query_assigned_licenses(mo_id, query_assigned_licenses_request_type)

Get information about all the licenses associated with an entity 

Get information about all the licenses associated with an entity  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_assignment_manager_license_assignment import LicenseAssignmentManagerLicenseAssignment
from vmware_vi.models.query_assigned_licenses_request_type import QueryAssignedLicensesRequestType
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
    api_instance = vmware_vi.LicenseAssignmentManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_assigned_licenses_request_type = vmware_vi.QueryAssignedLicensesRequestType() # QueryAssignedLicensesRequestType | 

    try:
        # Get information about all the licenses associated with an entity 
        api_response = api_instance.license_assignment_manager_query_assigned_licenses(mo_id, query_assigned_licenses_request_type)
        print("The response of LicenseAssignmentManagerApi->license_assignment_manager_query_assigned_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseAssignmentManagerApi->license_assignment_manager_query_assigned_licenses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_assigned_licenses_request_type** | [**QueryAssignedLicensesRequestType**](QueryAssignedLicensesRequestType.md)|  | 

### Return type

[**List[LicenseAssignmentManagerLicenseAssignment]**](LicenseAssignmentManagerLicenseAssignment.md)

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

# **license_assignment_manager_remove_assigned_license**
> license_assignment_manager_remove_assigned_license(mo_id, remove_assigned_license_request_type)

Remove licenses associated with an entity 

Remove licenses associated with an entity  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_assigned_license_request_type import RemoveAssignedLicenseRequestType
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
    api_instance = vmware_vi.LicenseAssignmentManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_assigned_license_request_type = vmware_vi.RemoveAssignedLicenseRequestType() # RemoveAssignedLicenseRequestType | 

    try:
        # Remove licenses associated with an entity 
        api_instance.license_assignment_manager_remove_assigned_license(mo_id, remove_assigned_license_request_type)
    except Exception as e:
        print("Exception when calling LicenseAssignmentManagerApi->license_assignment_manager_remove_assigned_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_assigned_license_request_type** | [**RemoveAssignedLicenseRequestType**](RemoveAssignedLicenseRequestType.md)|  | 

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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_assignment_manager_update_assigned_license**
> LicenseManagerLicenseInfo license_assignment_manager_update_assigned_license(mo_id, update_assigned_license_request_type)

Update the license associated with an entity 

Update the license associated with an entity  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo
from vmware_vi.models.update_assigned_license_request_type import UpdateAssignedLicenseRequestType
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
    api_instance = vmware_vi.LicenseAssignmentManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_assigned_license_request_type = vmware_vi.UpdateAssignedLicenseRequestType() # UpdateAssignedLicenseRequestType | 

    try:
        # Update the license associated with an entity 
        api_response = api_instance.license_assignment_manager_update_assigned_license(mo_id, update_assigned_license_request_type)
        print("The response of LicenseAssignmentManagerApi->license_assignment_manager_update_assigned_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseAssignmentManagerApi->license_assignment_manager_update_assigned_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_assigned_license_request_type** | [**UpdateAssignedLicenseRequestType**](UpdateAssignedLicenseRequestType.md)|  | 

### Return type

[**LicenseManagerLicenseInfo**](LicenseManagerLicenseInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns information about the license specified in licenseKey  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

