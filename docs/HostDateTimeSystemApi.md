# vmware_vi.HostDateTimeSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_date_time_system_get_date_time_info**](HostDateTimeSystemApi.md#host_date_time_system_get_date_time_info) | **GET** /HostDateTimeSystem/{moId}/dateTimeInfo | The DateTime configuration of the host. 
[**host_date_time_system_query_available_time_zones**](HostDateTimeSystemApi.md#host_date_time_system_query_available_time_zones) | **POST** /HostDateTimeSystem/{moId}/QueryAvailableTimeZones | Retrieves the list of available timezones on the host. 
[**host_date_time_system_query_date_time**](HostDateTimeSystemApi.md#host_date_time_system_query_date_time) | **POST** /HostDateTimeSystem/{moId}/QueryDateTime | Get the current DateTime on the host. 
[**host_date_time_system_refresh_date_time_system**](HostDateTimeSystemApi.md#host_date_time_system_refresh_date_time_system) | **POST** /HostDateTimeSystem/{moId}/RefreshDateTimeSystem | Refresh the DateTime related settings to pick up any changes that might have occurred. 
[**host_date_time_system_test_time_service**](HostDateTimeSystemApi.md#host_date_time_system_test_time_service) | **POST** /HostDateTimeSystem/{moId}/TestTimeService | Run a test to validate current time service configuration is functioning normally. 
[**host_date_time_system_update_date_time**](HostDateTimeSystemApi.md#host_date_time_system_update_date_time) | **POST** /HostDateTimeSystem/{moId}/UpdateDateTime | Update the date/time on the host. 
[**host_date_time_system_update_date_time_config**](HostDateTimeSystemApi.md#host_date_time_system_update_date_time_config) | **POST** /HostDateTimeSystem/{moId}/UpdateDateTimeConfig | Update the DateTime configuration of the host. 


# **host_date_time_system_get_date_time_info**
> HostDateTimeInfo host_date_time_system_get_date_time_info(mo_id)

The DateTime configuration of the host. 

The DateTime configuration of the host.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_date_time_info import HostDateTimeInfo
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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The DateTime configuration of the host. 
        api_response = api_instance.host_date_time_system_get_date_time_info(mo_id)
        print("The response of HostDateTimeSystemApi->host_date_time_system_get_date_time_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_get_date_time_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostDateTimeInfo**](HostDateTimeInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DateTime configuration of the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_date_time_system_query_available_time_zones**
> List[HostDateTimeSystemTimeZone] host_date_time_system_query_available_time_zones(mo_id)

Retrieves the list of available timezones on the host. 

Retrieves the list of available timezones on the host.  The API works off the public domain 'tz' timezone database.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_date_time_system_time_zone import HostDateTimeSystemTimeZone
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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieves the list of available timezones on the host. 
        api_response = api_instance.host_date_time_system_query_available_time_zones(mo_id)
        print("The response of HostDateTimeSystemApi->host_date_time_system_query_available_time_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_query_available_time_zones: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostDateTimeSystemTimeZone]**](HostDateTimeSystemTimeZone.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available timezones on the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_date_time_system_query_date_time**
> datetime host_date_time_system_query_date_time(mo_id)

Get the current DateTime on the host. 

Get the current DateTime on the host.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the current DateTime on the host. 
        api_response = api_instance.host_date_time_system_query_date_time(mo_id)
        print("The response of HostDateTimeSystemApi->host_date_time_system_query_date_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_query_date_time: %s\n" % e)
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
**200** | Current DateTime on the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_date_time_system_refresh_date_time_system**
> host_date_time_system_refresh_date_time_system(mo_id)

Refresh the DateTime related settings to pick up any changes that might have occurred. 

Refresh the DateTime related settings to pick up any changes that might have occurred.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.DateTime 

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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Refresh the DateTime related settings to pick up any changes that might have occurred. 
        api_instance.host_date_time_system_refresh_date_time_system(mo_id)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_refresh_date_time_system: %s\n" % e)
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

# **host_date_time_system_test_time_service**
> HostDateTimeSystemServiceTestResult host_date_time_system_test_time_service(mo_id)

Run a test to validate current time service configuration is functioning normally. 

Run a test to validate current time service configuration is functioning normally.  The report will provide a localized diagnostic of any issues. Only one diagnostic test may be running at a time.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Host.Config.DateTime 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_date_time_system_service_test_result import HostDateTimeSystemServiceTestResult
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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Run a test to validate current time service configuration is functioning normally. 
        api_response = api_instance.host_date_time_system_test_time_service(mo_id)
        print("The response of HostDateTimeSystemApi->host_date_time_system_test_time_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_test_time_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostDateTimeSystemServiceTestResult**](HostDateTimeSystemServiceTestResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the time service on this host based on present time service configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_date_time_system_update_date_time**
> host_date_time_system_update_date_time(mo_id, update_date_time_request_type)

Update the date/time on the host. 

Update the date/time on the host.  This method should be used with caution since network delays, execution delays can result in time skews.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.DateTime 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_date_time_request_type import UpdateDateTimeRequestType
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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_date_time_request_type = vmware_vi.UpdateDateTimeRequestType() # UpdateDateTimeRequestType | 

    try:
        # Update the date/time on the host. 
        api_instance.host_date_time_system_update_date_time(mo_id, update_date_time_request_type)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_update_date_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_date_time_request_type** | [**UpdateDateTimeRequestType**](UpdateDateTimeRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if an error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_date_time_system_update_date_time_config**
> host_date_time_system_update_date_time_config(mo_id, update_date_time_config_request_type)

Update the DateTime configuration of the host. 

Update the DateTime configuration of the host.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.DateTime 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_date_time_config_request_type import UpdateDateTimeConfigRequestType
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
    api_instance = vmware_vi.HostDateTimeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_date_time_config_request_type = vmware_vi.UpdateDateTimeConfigRequestType() # UpdateDateTimeConfigRequestType | 

    try:
        # Update the DateTime configuration of the host. 
        api_instance.host_date_time_system_update_date_time_config(mo_id, update_date_time_config_request_type)
    except Exception as e:
        print("Exception when calling HostDateTimeSystemApi->host_date_time_system_update_date_time_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_date_time_config_request_type** | [**UpdateDateTimeConfigRequestType**](UpdateDateTimeConfigRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if an error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

