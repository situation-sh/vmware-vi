# vmware_vi.OptionManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**option_manager_get_setting**](OptionManagerApi.md#option_manager_get_setting) | **GET** /OptionManager/{moId}/setting | A list of the current settings for the key/value pair options. 
[**option_manager_get_supported_option**](OptionManagerApi.md#option_manager_get_supported_option) | **GET** /OptionManager/{moId}/supportedOption | A list of supported key/value pair options including their type information. 
[**option_manager_query_options**](OptionManagerApi.md#option_manager_query_options) | **POST** /OptionManager/{moId}/QueryOptions | Returns a specific node or nodes in the option hierarchy. 
[**option_manager_update_options**](OptionManagerApi.md#option_manager_update_options) | **POST** /OptionManager/{moId}/UpdateOptions | Updates one or more options. 


# **option_manager_get_setting**
> List[OptionValue] option_manager_get_setting(mo_id)

A list of the current settings for the key/value pair options. 

A list of the current settings for the key/value pair options. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.option_value import OptionValue
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
    api_instance = vmware_vi.OptionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of the current settings for the key/value pair options. 
        api_response = api_instance.option_manager_get_setting(mo_id)
        print("The response of OptionManagerApi->option_manager_get_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionManagerApi->option_manager_get_setting: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[OptionValue]**](OptionValue.md)

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

# **option_manager_get_supported_option**
> List[OptionDef] option_manager_get_supported_option(mo_id)

A list of supported key/value pair options including their type information. 

A list of supported key/value pair options including their type information. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.option_def import OptionDef
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
    api_instance = vmware_vi.OptionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of supported key/value pair options including their type information. 
        api_response = api_instance.option_manager_get_supported_option(mo_id)
        print("The response of OptionManagerApi->option_manager_get_supported_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionManagerApi->option_manager_get_supported_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[OptionDef]**](OptionDef.md)

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

# **option_manager_query_options**
> List[OptionValue] option_manager_query_options(mo_id, query_options_request_type)

Returns a specific node or nodes in the option hierarchy. 

Returns a specific node or nodes in the option hierarchy.  This method might require any of the following privileges depending on where the property fits in the inventory tree. - System.View on the root folder, if this is used to read settings   in the &quot;client&quot; subtree. - System.Read on the root folder, if this is used to read all settings   or any settings beside those in the &quot;client&quot; subtree. - System.Read on the host, if this is used to read the advanced   options for a host configuration.    ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.option_value import OptionValue
from vmware_vi.models.query_options_request_type import QueryOptionsRequestType
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
    api_instance = vmware_vi.OptionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_options_request_type = vmware_vi.QueryOptionsRequestType() # QueryOptionsRequestType | 

    try:
        # Returns a specific node or nodes in the option hierarchy. 
        api_response = api_instance.option_manager_query_options(mo_id, query_options_request_type)
        print("The response of OptionManagerApi->option_manager_query_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionManagerApi->option_manager_query_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_options_request_type** | [**QueryOptionsRequestType**](QueryOptionsRequestType.md)|  | 

### Return type

[**List[OptionValue]**](OptionValue.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The option with the given name. If the name ends with a dot, all options for that subtree are returned.  |  -  |
**500** | ***InvalidName***: if no option or subtree exists with the given name.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **option_manager_update_options**
> option_manager_update_options(mo_id, update_options_request_type)

Updates one or more options. 

Updates one or more options.  The options are changed one by one, and the operation is not atomic. This means that on failure some of the options may not be changed.  A nested option setting can be named using a dot notation; for example, system.cacheSize.  This method might require any of the following privileges depending on where the property fits in the inventory tree. - Global.Settings on the root folder, if this is used to modify the   settings in the service node. - Host.Config.AdvancedConfig on the host, if this is used to set the   advanced options in the host configuration. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_options_request_type import UpdateOptionsRequestType
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
    api_instance = vmware_vi.OptionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_options_request_type = vmware_vi.UpdateOptionsRequestType() # UpdateOptionsRequestType | 

    try:
        # Updates one or more options. 
        api_instance.option_manager_update_options(mo_id, update_options_request_type)
    except Exception as e:
        print("Exception when calling OptionManagerApi->option_manager_update_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_options_request_type** | [**UpdateOptionsRequestType**](UpdateOptionsRequestType.md)|  | 

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
**500** | ***InvalidName***: if one or more OptionValue objects refers to a non-existent option.  ***InvalidArgument***: if one or more OptionValue contains an invalid value.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

