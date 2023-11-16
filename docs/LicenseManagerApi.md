# vmware_vi.LicenseManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_manager_add_license**](LicenseManagerApi.md#license_manager_add_license) | **POST** /LicenseManager/{moId}/AddLicense | Adds a license to the inventory of available licenses. 
[**license_manager_check_license_feature**](LicenseManagerApi.md#license_manager_check_license_feature) | **POST** /LicenseManager/{moId}/CheckLicenseFeature | Returns whether or not a given feature is enabled. 
[**license_manager_configure_license_source**](LicenseManagerApi.md#license_manager_configure_license_source) | **POST** /LicenseManager/{moId}/ConfigureLicenseSource | Allows for reconfiguration of the License Manager license source. 
[**license_manager_decode_license**](LicenseManagerApi.md#license_manager_decode_license) | **POST** /LicenseManager/{moId}/DecodeLicense | Decodes licensing information on the license specified. 
[**license_manager_disable_feature**](LicenseManagerApi.md#license_manager_disable_feature) | **POST** /LicenseManager/{moId}/DisableFeature | Release licenses for an optional feature. 
[**license_manager_enable_feature**](LicenseManagerApi.md#license_manager_enable_feature) | **POST** /LicenseManager/{moId}/EnableFeature | Enable a feature that has an optional state. 
[**license_manager_get_diagnostics**](LicenseManagerApi.md#license_manager_get_diagnostics) | **GET** /LicenseManager/{moId}/diagnostics | Return current diagnostic information. 
[**license_manager_get_evaluation**](LicenseManagerApi.md#license_manager_get_evaluation) | **GET** /LicenseManager/{moId}/evaluation | 
[**license_manager_get_feature_info**](LicenseManagerApi.md#license_manager_get_feature_info) | **GET** /LicenseManager/{moId}/featureInfo | The list of features that can be licensed. 
[**license_manager_get_license_assignment_manager**](LicenseManagerApi.md#license_manager_get_license_assignment_manager) | **GET** /LicenseManager/{moId}/licenseAssignmentManager | License Assignment Manager 
[**license_manager_get_licensed_edition**](LicenseManagerApi.md#license_manager_get_licensed_edition) | **GET** /LicenseManager/{moId}/licensedEdition | The product&#39;s license edition. 
[**license_manager_get_licenses**](LicenseManagerApi.md#license_manager_get_licenses) | **GET** /LicenseManager/{moId}/licenses | Get information about all the licenses available. 
[**license_manager_get_source**](LicenseManagerApi.md#license_manager_get_source) | **GET** /LicenseManager/{moId}/source | Set or return a data object type of LocalLicense or LicenseServer. 
[**license_manager_get_source_available**](LicenseManagerApi.md#license_manager_get_source_available) | **GET** /LicenseManager/{moId}/sourceAvailable | Current state of the license source. 
[**license_manager_query_license_source_availability**](LicenseManagerApi.md#license_manager_query_license_source_availability) | **POST** /LicenseManager/{moId}/QueryLicenseSourceAvailability | Queries the current license source for total and available licenses available for each feature known to this system. 
[**license_manager_query_license_usage**](LicenseManagerApi.md#license_manager_query_license_usage) | **POST** /LicenseManager/{moId}/QueryLicenseUsage | Returns the license usage. 
[**license_manager_query_supported_features**](LicenseManagerApi.md#license_manager_query_supported_features) | **POST** /LicenseManager/{moId}/QuerySupportedFeatures | Queries the current license source for a list of available licenses that can be licensed from this system. 
[**license_manager_remove_license**](LicenseManagerApi.md#license_manager_remove_license) | **POST** /LicenseManager/{moId}/RemoveLicense | Remove license from the available set. 
[**license_manager_remove_license_label**](LicenseManagerApi.md#license_manager_remove_license_label) | **POST** /LicenseManager/{moId}/RemoveLicenseLabel | Removed a license&#39;s label. 
[**license_manager_set_license_edition**](LicenseManagerApi.md#license_manager_set_license_edition) | **POST** /LicenseManager/{moId}/SetLicenseEdition | Defines the product&#39;s license edition. 
[**license_manager_update_license**](LicenseManagerApi.md#license_manager_update_license) | **POST** /LicenseManager/{moId}/UpdateLicense | Updates the available licenses to the one provided in licenseKey. 
[**license_manager_update_license_label**](LicenseManagerApi.md#license_manager_update_license_label) | **POST** /LicenseManager/{moId}/UpdateLicenseLabel | Update a license&#39;s label. 


# **license_manager_add_license**
> LicenseManagerLicenseInfo license_manager_add_license(mo_id, add_license_request_type)

Adds a license to the inventory of available licenses. 

Adds a license to the inventory of available licenses.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_license_request_type import AddLicenseRequestType
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_license_request_type = vmware_vi.AddLicenseRequestType() # AddLicenseRequestType | 

    try:
        # Adds a license to the inventory of available licenses. 
        api_response = api_instance.license_manager_add_license(mo_id, add_license_request_type)
        print("The response of LicenseManagerApi->license_manager_add_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_add_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_license_request_type** | [**AddLicenseRequestType**](AddLicenseRequestType.md)|  | 

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
**200** | Returns information about the license specified in licenseKey.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_check_license_feature**
> bool license_manager_check_license_feature(mo_id, check_license_feature_request_type)

Returns whether or not a given feature is enabled. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  Returns whether or not a given feature is enabled.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_license_feature_request_type import CheckLicenseFeatureRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_license_feature_request_type = vmware_vi.CheckLicenseFeatureRequestType() # CheckLicenseFeatureRequestType | 

    try:
        # Returns whether or not a given feature is enabled. 
        api_response = api_instance.license_manager_check_license_feature(mo_id, check_license_feature_request_type)
        print("The response of LicenseManagerApi->license_manager_check_license_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_check_license_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_license_feature_request_type** | [**CheckLicenseFeatureRequestType**](CheckLicenseFeatureRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns true if the feature is enabled and false if it is not.  |  -  |
**500** | ***InvalidArgument***: If a feature name is not found.  ***InvalidState***: If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_configure_license_source**
> license_manager_configure_license_source(mo_id, configure_license_source_request_type)

Allows for reconfiguration of the License Manager license source. 

Deprecated as of vSphere API 4.0, use *LicenseManager.UpdateLicense* instead.  Allows for reconfiguration of the License Manager license source.  This changes the licensing source to be either served or local. Before changing the license source location, the API checks the number of licenses available at the new potential source to ensure there are at least as many licenses there as have been issued by the current source. If there are an equal or greater number of licenses at the new source, all licenses on the current source are released and then reacquired from the new source. If there are not enough licenses available on the new source to reissue all licenses, the operation fails.  This is used to configure the license source on an individual host.  **PLATFORM Specific Notes:** VirtualCenter - only supports a served source. the host parameter is mandatory. ESX Server - the host parameter is optional.  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_license_source_request_type import ConfigureLicenseSourceRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_license_source_request_type = vmware_vi.ConfigureLicenseSourceRequestType() # ConfigureLicenseSourceRequestType | 

    try:
        # Allows for reconfiguration of the License Manager license source. 
        api_instance.license_manager_configure_license_source(mo_id, configure_license_source_request_type)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_configure_license_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_license_source_request_type** | [**ConfigureLicenseSourceRequestType**](ConfigureLicenseSourceRequestType.md)|  | 

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
**500** | ***LicenseServerUnavailable***: if the license server is unreachable.  ***CannotAccessLocalSource***: if the local source cannot be accessed.  ***InvalidLicense***: if the new license source is LocalLicenseSource and the license file is not valid.  ***NotEnoughLicenses***: if the new license source does not have enough licenses.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_decode_license**
> LicenseManagerLicenseInfo license_manager_decode_license(mo_id, decode_license_request_type)

Decodes licensing information on the license specified. 

Decodes licensing information on the license specified.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.decode_license_request_type import DecodeLicenseRequestType
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    decode_license_request_type = vmware_vi.DecodeLicenseRequestType() # DecodeLicenseRequestType | 

    try:
        # Decodes licensing information on the license specified. 
        api_response = api_instance.license_manager_decode_license(mo_id, decode_license_request_type)
        print("The response of LicenseManagerApi->license_manager_decode_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_decode_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **decode_license_request_type** | [**DecodeLicenseRequestType**](DecodeLicenseRequestType.md)|  | 

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
**200** | Returns information about the license specified in licenseKey.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_disable_feature**
> bool license_manager_disable_feature(mo_id, disable_feature_request_type)

Release licenses for an optional feature. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.RemoveAssignedLicense* instead.  Release licenses for an optional feature.  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disable_feature_request_type import DisableFeatureRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disable_feature_request_type = vmware_vi.DisableFeatureRequestType() # DisableFeatureRequestType | 

    try:
        # Release licenses for an optional feature. 
        api_response = api_instance.license_manager_disable_feature(mo_id, disable_feature_request_type)
        print("The response of LicenseManagerApi->license_manager_disable_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_disable_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disable_feature_request_type** | [**DisableFeatureRequestType**](DisableFeatureRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns true if the feature was disabled and false if not.  |  -  |
**500** | ***InvalidArgument***: If a feature name is not found or it is not optional.  ***LicenseServerUnavailable***: If the license server is unavailable.  ***InvalidState***: If the feature is in use.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_enable_feature**
> bool license_manager_enable_feature(mo_id, enable_feature_request_type)

Enable a feature that has an optional state. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.UpdateAssignedLicense* instead.  Enable a feature that has an optional state.  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_feature_request_type import EnableFeatureRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_feature_request_type = vmware_vi.EnableFeatureRequestType() # EnableFeatureRequestType | 

    try:
        # Enable a feature that has an optional state. 
        api_response = api_instance.license_manager_enable_feature(mo_id, enable_feature_request_type)
        print("The response of LicenseManagerApi->license_manager_enable_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_enable_feature: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_feature_request_type** | [**EnableFeatureRequestType**](EnableFeatureRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns true if enabling the feature was successful, false otherwise.  |  -  |
**500** | ***InvalidArgument***: If a feature name is not found or it is not optional.  ***LicenseServerUnavailable***: If the license server is unavailable.  ***InvalidState***: If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_get_diagnostics**
> LicenseDiagnostics license_manager_get_diagnostics(mo_id)

Return current diagnostic information. 

Deprecated as of vSphere API 4.0, this property is not used by the system.  Return current diagnostic information.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_diagnostics import LicenseDiagnostics
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Return current diagnostic information. 
        api_response = api_instance.license_manager_get_diagnostics(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_diagnostics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_diagnostics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**LicenseDiagnostics**](LicenseDiagnostics.md)

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

# **license_manager_get_evaluation**
> LicenseManagerEvaluationInfo license_manager_get_evaluation(mo_id)



***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_manager_evaluation_info import LicenseManagerEvaluationInfo
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        api_response = api_instance.license_manager_get_evaluation(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_evaluation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**LicenseManagerEvaluationInfo**](LicenseManagerEvaluationInfo.md)

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

# **license_manager_get_feature_info**
> List[LicenseFeatureInfo] license_manager_get_feature_info(mo_id)

The list of features that can be licensed. 

Deprecated as of VI API 2.5, use *LicenseManager.QuerySupportedFeatures* instead.  The list of features that can be licensed. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_feature_info import LicenseFeatureInfo
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of features that can be licensed. 
        api_response = api_instance.license_manager_get_feature_info(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_feature_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_feature_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[LicenseFeatureInfo]**](LicenseFeatureInfo.md)

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

# **license_manager_get_license_assignment_manager**
> ManagedObjectReference license_manager_get_license_assignment_manager(mo_id)

License Assignment Manager 

License Assignment Manager  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # License Assignment Manager 
        api_response = api_instance.license_manager_get_license_assignment_manager(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_license_assignment_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_license_assignment_manager: %s\n" % e)
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
**200** | Refers instance of *LicenseAssignmentManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_get_licensed_edition**
> str license_manager_get_licensed_edition(mo_id)

The product's license edition. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  The product's license edition.  The edition defines which product license the server requires. This, in turn, determines the core set of functionalities provided by the product and the additional features that can be licensed. If no edition is set the property is set to the empty string (\"\"). To set the edition use *LicenseManager.SetLicenseEdition*.  ***Since:*** VI API 2.5 

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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The product's license edition. 
        api_response = api_instance.license_manager_get_licensed_edition(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_licensed_edition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_licensed_edition: %s\n" % e)
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

# **license_manager_get_licenses**
> List[LicenseManagerLicenseInfo] license_manager_get_licenses(mo_id)

Get information about all the licenses available. 

Get information about all the licenses available.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get information about all the licenses available. 
        api_response = api_instance.license_manager_get_licenses(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_licenses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[LicenseManagerLicenseInfo]**](LicenseManagerLicenseInfo.md)

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

# **license_manager_get_source**
> LicenseSource license_manager_get_source(mo_id)

Set or return a data object type of LocalLicense or LicenseServer. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* to get evaluation information.  Set or return a data object type of LocalLicense or LicenseServer. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_source import LicenseSource
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Set or return a data object type of LocalLicense or LicenseServer. 
        api_response = api_instance.license_manager_get_source(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**LicenseSource**](LicenseSource.md)

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

# **license_manager_get_source_available**
> bool license_manager_get_source_available(mo_id)

Current state of the license source. 

Deprecated as of vSphere API 4.0, this property is not used.  Current state of the license source.  License sources that are LocalSource are always available. 

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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current state of the license source. 
        api_response = api_instance.license_manager_get_source_available(mo_id)
        print("The response of LicenseManagerApi->license_manager_get_source_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_get_source_available: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**bool**

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

# **license_manager_query_license_source_availability**
> List[LicenseAvailabilityInfo] license_manager_query_license_source_availability(mo_id, query_license_source_availability_request_type)

Queries the current license source for total and available licenses available for each feature known to this system. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  Queries the current license source for total and available licenses available for each feature known to this system.  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_availability_info import LicenseAvailabilityInfo
from vmware_vi.models.query_license_source_availability_request_type import QueryLicenseSourceAvailabilityRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_license_source_availability_request_type = vmware_vi.QueryLicenseSourceAvailabilityRequestType() # QueryLicenseSourceAvailabilityRequestType | 

    try:
        # Queries the current license source for total and available licenses available for each feature known to this system. 
        api_response = api_instance.license_manager_query_license_source_availability(mo_id, query_license_source_availability_request_type)
        print("The response of LicenseManagerApi->license_manager_query_license_source_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_query_license_source_availability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_license_source_availability_request_type** | [**QueryLicenseSourceAvailabilityRequestType**](QueryLicenseSourceAvailabilityRequestType.md)|  | 

### Return type

[**List[LicenseAvailabilityInfo]**](LicenseAvailabilityInfo.md)

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

# **license_manager_query_license_usage**
> LicenseUsageInfo license_manager_query_license_usage(mo_id, query_license_usage_request_type)

Returns the license usage. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  Returns the license usage.  The license usage is a list of supported features and the number of licenses that have been reserved.  **PLATFORM Specific Notes:** VirtualCenter - Empty string returns the usage of non-host specific features. Must specify managed host to query. ESX Server - Host argument ignored.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_usage_info import LicenseUsageInfo
from vmware_vi.models.query_license_usage_request_type import QueryLicenseUsageRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_license_usage_request_type = vmware_vi.QueryLicenseUsageRequestType() # QueryLicenseUsageRequestType | 

    try:
        # Returns the license usage. 
        api_response = api_instance.license_manager_query_license_usage(mo_id, query_license_usage_request_type)
        print("The response of LicenseManagerApi->license_manager_query_license_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_query_license_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_license_usage_request_type** | [**QueryLicenseUsageRequestType**](QueryLicenseUsageRequestType.md)|  | 

### Return type

[**LicenseUsageInfo**](LicenseUsageInfo.md)

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

# **license_manager_query_supported_features**
> List[LicenseFeatureInfo] license_manager_query_supported_features(mo_id, query_supported_features_request_type)

Queries the current license source for a list of available licenses that can be licensed from this system. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  Queries the current license source for a list of available licenses that can be licensed from this system.  ***Since:*** VI API 2.5  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_feature_info import LicenseFeatureInfo
from vmware_vi.models.query_supported_features_request_type import QuerySupportedFeaturesRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_supported_features_request_type = vmware_vi.QuerySupportedFeaturesRequestType() # QuerySupportedFeaturesRequestType | 

    try:
        # Queries the current license source for a list of available licenses that can be licensed from this system. 
        api_response = api_instance.license_manager_query_supported_features(mo_id, query_supported_features_request_type)
        print("The response of LicenseManagerApi->license_manager_query_supported_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_query_supported_features: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_supported_features_request_type** | [**QuerySupportedFeaturesRequestType**](QuerySupportedFeaturesRequestType.md)|  | 

### Return type

[**List[LicenseFeatureInfo]**](LicenseFeatureInfo.md)

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

# **license_manager_remove_license**
> license_manager_remove_license(mo_id, remove_license_request_type)

Remove license from the available set. 

Remove license from the available set.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_license_request_type import RemoveLicenseRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_license_request_type = vmware_vi.RemoveLicenseRequestType() # RemoveLicenseRequestType | 

    try:
        # Remove license from the available set. 
        api_instance.license_manager_remove_license(mo_id, remove_license_request_type)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_remove_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_license_request_type** | [**RemoveLicenseRequestType**](RemoveLicenseRequestType.md)|  | 

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

# **license_manager_remove_license_label**
> license_manager_remove_license_label(mo_id, remove_license_label_request_type)

Removed a license's label. 

Removed a license's label.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_license_label_request_type import RemoveLicenseLabelRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_license_label_request_type = vmware_vi.RemoveLicenseLabelRequestType() # RemoveLicenseLabelRequestType | 

    try:
        # Removed a license's label. 
        api_instance.license_manager_remove_license_label(mo_id, remove_license_label_request_type)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_remove_license_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_license_label_request_type** | [**RemoveLicenseLabelRequestType**](RemoveLicenseLabelRequestType.md)|  | 

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

# **license_manager_set_license_edition**
> license_manager_set_license_edition(mo_id, set_license_edition_request_type)

Defines the product's license edition. 

Deprecated as of vSphere API 4.0, use *LicenseAssignmentManager.QueryAssignedLicenses* instead.  Defines the product's license edition.  The edition defines which product license the server requires. This, in turn, determines the core set of functionality provided by the product and the additional features that can be licensed.  To determine what featureKey the current platform will accept, use querySourceAvailablity() at runtime, or consult the documentation for the current platform.  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_license_edition_request_type import SetLicenseEditionRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_license_edition_request_type = vmware_vi.SetLicenseEditionRequestType() # SetLicenseEditionRequestType | 

    try:
        # Defines the product's license edition. 
        api_instance.license_manager_set_license_edition(mo_id, set_license_edition_request_type)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_set_license_edition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_license_edition_request_type** | [**SetLicenseEditionRequestType**](SetLicenseEditionRequestType.md)|  | 

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
**500** | ***InvalidArgument***: If a feature key is not an edition feature key.  ***LicenseServerUnavailable***: If the license server is unavailable.  ***InvalidState***: If the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_update_license**
> LicenseManagerLicenseInfo license_manager_update_license(mo_id, update_license_request_type)

Updates the available licenses to the one provided in licenseKey. 

Updates the available licenses to the one provided in licenseKey.  This is the same as removing all the licenses using *LicenseManager.RemoveLicense* and adding licenseKey using *LicenseManager.AddLicense* If the optional parameter labels is specify this is the same as calling updateLicense without the optioal parameter and calling updateLabel for each pair in the labels array.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo
from vmware_vi.models.update_license_request_type import UpdateLicenseRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_license_request_type = vmware_vi.UpdateLicenseRequestType() # UpdateLicenseRequestType | 

    try:
        # Updates the available licenses to the one provided in licenseKey. 
        api_response = api_instance.license_manager_update_license(mo_id, update_license_request_type)
        print("The response of LicenseManagerApi->license_manager_update_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_update_license: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_license_request_type** | [**UpdateLicenseRequestType**](UpdateLicenseRequestType.md)|  | 

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
**200** | Returns information about the license specified in licenseKey.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_manager_update_license_label**
> license_manager_update_license_label(mo_id, update_license_label_request_type)

Update a license's label. 

Update a license's label.  It creates a label entry if the labelKey doesn't already exist  ***Since:*** vSphere API 4.0  ***Required privileges:*** Global.Licenses 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_license_label_request_type import UpdateLicenseLabelRequestType
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
    api_instance = vmware_vi.LicenseManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_license_label_request_type = vmware_vi.UpdateLicenseLabelRequestType() # UpdateLicenseLabelRequestType | 

    try:
        # Update a license's label. 
        api_instance.license_manager_update_license_label(mo_id, update_license_label_request_type)
    except Exception as e:
        print("Exception when calling LicenseManagerApi->license_manager_update_license_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_license_label_request_type** | [**UpdateLicenseLabelRequestType**](UpdateLicenseLabelRequestType.md)|  | 

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

