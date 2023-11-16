# vmware_vi.HostFirmwareSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_firmware_system_backup_firmware_configuration**](HostFirmwareSystemApi.md#host_firmware_system_backup_firmware_configuration) | **POST** /HostFirmwareSystem/{moId}/BackupFirmwareConfiguration | Backup the configuration of the host. 
[**host_firmware_system_query_firmware_config_upload_url**](HostFirmwareSystemApi.md#host_firmware_system_query_firmware_config_upload_url) | **POST** /HostFirmwareSystem/{moId}/QueryFirmwareConfigUploadURL | Return the URL on the host to which the configuration bundle must be uploaded for a restore operation. 
[**host_firmware_system_reset_firmware_to_factory_defaults**](HostFirmwareSystemApi.md#host_firmware_system_reset_firmware_to_factory_defaults) | **POST** /HostFirmwareSystem/{moId}/ResetFirmwareToFactoryDefaults | Reset the configuration to factory defaults. 
[**host_firmware_system_restore_firmware_configuration**](HostFirmwareSystemApi.md#host_firmware_system_restore_firmware_configuration) | **POST** /HostFirmwareSystem/{moId}/RestoreFirmwareConfiguration | Restore the configuration of the host to that specified in the bundle. 


# **host_firmware_system_backup_firmware_configuration**
> str host_firmware_system_backup_firmware_configuration(mo_id)

Backup the configuration of the host. 

Backup the configuration of the host.  The method generates a bundle containing the host configuration. You can use an HTTP GET operation to download the bundle from the returned URL.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Firmware 

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
    api_instance = vmware_vi.HostFirmwareSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Backup the configuration of the host. 
        api_response = api_instance.host_firmware_system_backup_firmware_configuration(mo_id)
        print("The response of HostFirmwareSystemApi->host_firmware_system_backup_firmware_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostFirmwareSystemApi->host_firmware_system_backup_firmware_configuration: %s\n" % e)
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
**200** | URL that identifies the location of the backup bundle.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_firmware_system_query_firmware_config_upload_url**
> str host_firmware_system_query_firmware_config_upload_url(mo_id)

Return the URL on the host to which the configuration bundle must be uploaded for a restore operation. 

Return the URL on the host to which the configuration bundle must be uploaded for a restore operation.  See *HostFirmwareSystem.RestoreFirmwareConfiguration*.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Firmware 

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
    api_instance = vmware_vi.HostFirmwareSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Return the URL on the host to which the configuration bundle must be uploaded for a restore operation. 
        api_response = api_instance.host_firmware_system_query_firmware_config_upload_url(mo_id)
        print("The response of HostFirmwareSystemApi->host_firmware_system_query_firmware_config_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostFirmwareSystemApi->host_firmware_system_query_firmware_config_upload_url: %s\n" % e)
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
**200** | URL that identifies the location for the restore operation.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_firmware_system_reset_firmware_to_factory_defaults**
> host_firmware_system_reset_firmware_to_factory_defaults(mo_id)

Reset the configuration to factory defaults. 

Reset the configuration to factory defaults.  This method will reset all configuration options, including the \"admin\" password, to the factory defaults. The host will be rebooted immediately. The host needs to be in maintenance mode before this operation can be performed.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Firmware 

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
    api_instance = vmware_vi.HostFirmwareSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reset the configuration to factory defaults. 
        api_instance.host_firmware_system_reset_firmware_to_factory_defaults(mo_id)
    except Exception as e:
        print("Exception when calling HostFirmwareSystemApi->host_firmware_system_reset_firmware_to_factory_defaults: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidState***: if the host is not in maintenance mode.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_firmware_system_restore_firmware_configuration**
> host_firmware_system_restore_firmware_configuration(mo_id, restore_firmware_configuration_request_type)

Restore the configuration of the host to that specified in the bundle. 

Restore the configuration of the host to that specified in the bundle.  Upload the bundle to the URL returned by the *HostFirmwareSystem.QueryFirmwareConfigUploadURL* method. The *HostFirmwareSystem.RestoreFirmwareConfiguration* method will restore all configuration options, including the \"admin\" password, to the values in the bundle. The host will be rebooted immediately. The host must be in maintenance mode before this operation can be performed.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Firmware 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.restore_firmware_configuration_request_type import RestoreFirmwareConfigurationRequestType
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
    api_instance = vmware_vi.HostFirmwareSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    restore_firmware_configuration_request_type = vmware_vi.RestoreFirmwareConfigurationRequestType() # RestoreFirmwareConfigurationRequestType | 

    try:
        # Restore the configuration of the host to that specified in the bundle. 
        api_instance.host_firmware_system_restore_firmware_configuration(mo_id, restore_firmware_configuration_request_type)
    except Exception as e:
        print("Exception when calling HostFirmwareSystemApi->host_firmware_system_restore_firmware_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **restore_firmware_configuration_request_type** | [**RestoreFirmwareConfigurationRequestType**](RestoreFirmwareConfigurationRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host is not in maintenance mode.  ***FileFault***: if the file was not accessible.  ***MismatchedBundle***: if the uuid / build number in the bundle does not match the uuid / build number of the host and parameter &#39;force&#39; is set to false.  ***InvalidBundle***: if the bundle does not have the expected contents.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

