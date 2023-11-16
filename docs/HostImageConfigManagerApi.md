# vmware_vi.HostImageConfigManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_image_config_manager_fetch_software_packages**](HostImageConfigManagerApi.md#host_image_config_manager_fetch_software_packages) | **POST** /HostImageConfigManager/{moId}/fetchSoftwarePackages | Reports the set of software packages installed. 
[**host_image_config_manager_host_image_config_get_acceptance**](HostImageConfigManagerApi.md#host_image_config_manager_host_image_config_get_acceptance) | **POST** /HostImageConfigManager/{moId}/HostImageConfigGetAcceptance | Queries the current host acceptance level setting. 
[**host_image_config_manager_host_image_config_get_profile**](HostImageConfigManagerApi.md#host_image_config_manager_host_image_config_get_profile) | **POST** /HostImageConfigManager/{moId}/HostImageConfigGetProfile | Queries the current host image profile information. 
[**host_image_config_manager_install_date**](HostImageConfigManagerApi.md#host_image_config_manager_install_date) | **POST** /HostImageConfigManager/{moId}/installDate | Reports the UTC time stamp when this system was first installed. 
[**host_image_config_manager_update_host_image_acceptance_level**](HostImageConfigManagerApi.md#host_image_config_manager_update_host_image_acceptance_level) | **POST** /HostImageConfigManager/{moId}/UpdateHostImageAcceptanceLevel | Sets the acceptance level of the host image profile. 


# **host_image_config_manager_fetch_software_packages**
> List[SoftwarePackage] host_image_config_manager_fetch_software_packages(mo_id)

Reports the set of software packages installed. 

Reports the set of software packages installed.  The CLI command is: esxcli software vib get  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Config.Image 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.software_package import SoftwarePackage
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
    api_instance = vmware_vi.HostImageConfigManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reports the set of software packages installed. 
        api_response = api_instance.host_image_config_manager_fetch_software_packages(mo_id)
        print("The response of HostImageConfigManagerApi->host_image_config_manager_fetch_software_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostImageConfigManagerApi->host_image_config_manager_fetch_software_packages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[SoftwarePackage]**](SoftwarePackage.md)

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

# **host_image_config_manager_host_image_config_get_acceptance**
> str host_image_config_manager_host_image_config_get_acceptance(mo_id)

Queries the current host acceptance level setting. 

Queries the current host acceptance level setting.  See also *HostImageAcceptanceLevel_enum*If this has not been configured yet, then a default value will be returned..  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.HostImageConfigManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Queries the current host acceptance level setting. 
        api_response = api_instance.host_image_config_manager_host_image_config_get_acceptance(mo_id)
        print("The response of HostImageConfigManagerApi->host_image_config_manager_host_image_config_get_acceptance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostImageConfigManagerApi->host_image_config_manager_host_image_config_get_acceptance: %s\n" % e)
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
**500** | ***HostConfigFault***: if the host acceptance setting is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_image_config_manager_host_image_config_get_profile**
> HostImageProfileSummary host_image_config_manager_host_image_config_get_profile(mo_id)

Queries the current host image profile information. 

Queries the current host image profile information.  See also *HostImageProfileSummary*If there is no host image profile, then the value \"&lt;Unknown&gt;\" will populate both name and vendor..  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_image_profile_summary import HostImageProfileSummary
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
    api_instance = vmware_vi.HostImageConfigManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Queries the current host image profile information. 
        api_response = api_instance.host_image_config_manager_host_image_config_get_profile(mo_id)
        print("The response of HostImageConfigManagerApi->host_image_config_manager_host_image_config_get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostImageConfigManagerApi->host_image_config_manager_host_image_config_get_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostImageProfileSummary**](HostImageProfileSummary.md)

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

# **host_image_config_manager_install_date**
> datetime host_image_config_manager_install_date(mo_id)

Reports the UTC time stamp when this system was first installed. 

Reports the UTC time stamp when this system was first installed.  The CLI command is: esxcli system stats installtime get  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Config.Image 

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
    api_instance = vmware_vi.HostImageConfigManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reports the UTC time stamp when this system was first installed. 
        api_response = api_instance.host_image_config_manager_install_date(mo_id)
        print("The response of HostImageConfigManagerApi->host_image_config_manager_install_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostImageConfigManagerApi->host_image_config_manager_install_date: %s\n" % e)
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

# **host_image_config_manager_update_host_image_acceptance_level**
> host_image_config_manager_update_host_image_acceptance_level(mo_id, update_host_image_acceptance_level_request_type)

Sets the acceptance level of the host image profile. 

Sets the acceptance level of the host image profile.  See also *HostImageAcceptanceLevel_enum*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Image 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_host_image_acceptance_level_request_type import UpdateHostImageAcceptanceLevelRequestType
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
    api_instance = vmware_vi.HostImageConfigManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_host_image_acceptance_level_request_type = vmware_vi.UpdateHostImageAcceptanceLevelRequestType() # UpdateHostImageAcceptanceLevelRequestType | 

    try:
        # Sets the acceptance level of the host image profile. 
        api_instance.host_image_config_manager_update_host_image_acceptance_level(mo_id, update_host_image_acceptance_level_request_type)
    except Exception as e:
        print("Exception when calling HostImageConfigManagerApi->host_image_config_manager_update_host_image_acceptance_level: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_host_image_acceptance_level_request_type** | [**UpdateHostImageAcceptanceLevelRequestType**](UpdateHostImageAcceptanceLevelRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if the acceptance level is raised and there are VIB packages that are not permitted by the higher acceptance level.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

