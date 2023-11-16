# vmware_vi.OvfManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ovf_manager_create_descriptor**](OvfManagerApi.md#ovf_manager_create_descriptor) | **POST** /OvfManager/{moId}/CreateDescriptor | Create an OVF descriptor for the specified ManagedEntity, which may be a *VirtualMachine* or a *VirtualApp*. 
[**ovf_manager_create_import_spec**](OvfManagerApi.md#ovf_manager_create_import_spec) | **POST** /OvfManager/{moId}/CreateImportSpec | Validate the OVF descriptor against the hardware supported by the host system. 
[**ovf_manager_get_ovf_export_option**](OvfManagerApi.md#ovf_manager_get_ovf_export_option) | **GET** /OvfManager/{moId}/ovfExportOption | Returns an array of *OvfOptionInfo* object that specifies what options the server support for exporting an OVF descriptor. 
[**ovf_manager_get_ovf_import_option**](OvfManagerApi.md#ovf_manager_get_ovf_import_option) | **GET** /OvfManager/{moId}/ovfImportOption | Returns an array of *OvfOptionInfo* object that specifies what options the server support for modifing/relaxing the OVF import process. 
[**ovf_manager_parse_descriptor**](OvfManagerApi.md#ovf_manager_parse_descriptor) | **POST** /OvfManager/{moId}/ParseDescriptor | Parse the OVF descriptor and return as much information about it as possible without knowing the host on which it will be imported. 
[**ovf_manager_validate_host**](OvfManagerApi.md#ovf_manager_validate_host) | **POST** /OvfManager/{moId}/ValidateHost | Validate that the given OVF can be imported on the host. 


# **ovf_manager_create_descriptor**
> OvfCreateDescriptorResult ovf_manager_create_descriptor(mo_id, create_descriptor_request_type)

Create an OVF descriptor for the specified ManagedEntity, which may be a *VirtualMachine* or a *VirtualApp*. 

Create an OVF descriptor for the specified ManagedEntity, which may be a *VirtualMachine* or a *VirtualApp*.  To create the complete OVF descriptor, the client must already have downloaded the files that are part of the entity, because information about these files (compression, chunking, filename etc.) is part of the descriptor.  However, these downloads can be quite time-consuming, so if the descriptor for some reason cannot be generated, the client will want to know this before downloading the files.  For this reason, the client may do an initial \"dry run\" with the ovfFiles parameter unset. Default filenames will then be used in the descriptor, and the client can examine any warnings and/or errors before downloading the files.  After the final call to this method, client must release the lock on the entity given to it by *VirtualMachine.exportVm* or *VirtualApp.exportVApp*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_descriptor_request_type import CreateDescriptorRequestType
from vmware_vi.models.ovf_create_descriptor_result import OvfCreateDescriptorResult
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_descriptor_request_type = vmware_vi.CreateDescriptorRequestType() # CreateDescriptorRequestType | 

    try:
        # Create an OVF descriptor for the specified ManagedEntity, which may be a *VirtualMachine* or a *VirtualApp*. 
        api_response = api_instance.ovf_manager_create_descriptor(mo_id, create_descriptor_request_type)
        print("The response of OvfManagerApi->ovf_manager_create_descriptor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_create_descriptor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_descriptor_request_type** | [**CreateDescriptorRequestType**](CreateDescriptorRequestType.md)|  | 

### Return type

[**OvfCreateDescriptorResult**](OvfCreateDescriptorResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of CreateDescriptorResult  |  -  |
**500** | ***TaskInProgress***: if a required managed entity is busy.  ***VmConfigFault***: if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.  ***ConcurrentAccess***: if a concurrency issue prevents the operation from succeeding.  ***FileFault***: if there is a generic file error  ***InvalidState***: if the operation failed due to the current state of the system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ovf_manager_create_import_spec**
> OvfCreateImportSpecResult ovf_manager_create_import_spec(mo_id, create_import_spec_request_type)

Validate the OVF descriptor against the hardware supported by the host system. 

Validate the OVF descriptor against the hardware supported by the host system.  If the validation succeeds, return a result containing: - An *ImportSpec* to use when importing the entity. - A list of items to upload (for example disk backing files, ISO images etc.)    ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_import_spec_request_type import CreateImportSpecRequestType
from vmware_vi.models.ovf_create_import_spec_result import OvfCreateImportSpecResult
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_import_spec_request_type = vmware_vi.CreateImportSpecRequestType() # CreateImportSpecRequestType | 

    try:
        # Validate the OVF descriptor against the hardware supported by the host system. 
        api_response = api_instance.ovf_manager_create_import_spec(mo_id, create_import_spec_request_type)
        print("The response of OvfManagerApi->ovf_manager_create_import_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_create_import_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_import_spec_request_type** | [**CreateImportSpecRequestType**](CreateImportSpecRequestType.md)|  | 

### Return type

[**OvfCreateImportSpecResult**](OvfCreateImportSpecResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***TaskInProgress***: if a required managed entity is busy.  ***VmConfigFault***: if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.  ***ConcurrentAccess***: if a concurrency issue prevents the operation from succeeding.  ***FileFault***: if there is a generic file error  ***InvalidState***: if the operation failed due to the current state of the system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ovf_manager_get_ovf_export_option**
> List[OvfOptionInfo] ovf_manager_get_ovf_export_option(mo_id)

Returns an array of *OvfOptionInfo* object that specifies what options the server support for exporting an OVF descriptor. 

Returns an array of *OvfOptionInfo* object that specifies what options the server support for exporting an OVF descriptor.  ***Since:*** vSphere API 5.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ovf_option_info import OvfOptionInfo
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns an array of *OvfOptionInfo* object that specifies what options the server support for exporting an OVF descriptor. 
        api_response = api_instance.ovf_manager_get_ovf_export_option(mo_id)
        print("The response of OvfManagerApi->ovf_manager_get_ovf_export_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_get_ovf_export_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[OvfOptionInfo]**](OvfOptionInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of *OvfOptionInfo*  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ovf_manager_get_ovf_import_option**
> List[OvfOptionInfo] ovf_manager_get_ovf_import_option(mo_id)

Returns an array of *OvfOptionInfo* object that specifies what options the server support for modifing/relaxing the OVF import process. 

Returns an array of *OvfOptionInfo* object that specifies what options the server support for modifing/relaxing the OVF import process.  ***Since:*** vSphere API 5.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ovf_option_info import OvfOptionInfo
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns an array of *OvfOptionInfo* object that specifies what options the server support for modifing/relaxing the OVF import process. 
        api_response = api_instance.ovf_manager_get_ovf_import_option(mo_id)
        print("The response of OvfManagerApi->ovf_manager_get_ovf_import_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_get_ovf_import_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[OvfOptionInfo]**](OvfOptionInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of *OvfOptionInfo*  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ovf_manager_parse_descriptor**
> OvfParseDescriptorResult ovf_manager_parse_descriptor(mo_id, parse_descriptor_request_type)

Parse the OVF descriptor and return as much information about it as possible without knowing the host on which it will be imported. 

Parse the OVF descriptor and return as much information about it as possible without knowing the host on which it will be imported.  Typically, this method is called once without a deploymentOption parameter to obtain the values for the default deployment option. Part of the result is the list of possible deployment options. To obtain the values for a particular deployment option, call this method again, specifying that option.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ovf_parse_descriptor_result import OvfParseDescriptorResult
from vmware_vi.models.parse_descriptor_request_type import ParseDescriptorRequestType
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    parse_descriptor_request_type = vmware_vi.ParseDescriptorRequestType() # ParseDescriptorRequestType | 

    try:
        # Parse the OVF descriptor and return as much information about it as possible without knowing the host on which it will be imported. 
        api_response = api_instance.ovf_manager_parse_descriptor(mo_id, parse_descriptor_request_type)
        print("The response of OvfManagerApi->ovf_manager_parse_descriptor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_parse_descriptor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **parse_descriptor_request_type** | [**ParseDescriptorRequestType**](ParseDescriptorRequestType.md)|  | 

### Return type

[**OvfParseDescriptorResult**](OvfParseDescriptorResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the descriptor  |  -  |
**500** | ***TaskInProgress***: if a required managed entity is busy.  ***VmConfigFault***: if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.  ***ConcurrentAccess***: if a concurrency issue prevents the operation from succeeding.  ***FileFault***: if there is a generic file error  ***InvalidState***: if the operation failed due to the current state of the system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ovf_manager_validate_host**
> OvfValidateHostResult ovf_manager_validate_host(mo_id, validate_host_request_type)

Validate that the given OVF can be imported on the host. 

Validate that the given OVF can be imported on the host.  More specifically, this means whether or not the host supports the virtual hardware required by the OVF descriptor.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ovf_validate_host_result import OvfValidateHostResult
from vmware_vi.models.validate_host_request_type import ValidateHostRequestType
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
    api_instance = vmware_vi.OvfManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    validate_host_request_type = vmware_vi.ValidateHostRequestType() # ValidateHostRequestType | 

    try:
        # Validate that the given OVF can be imported on the host. 
        api_response = api_instance.ovf_manager_validate_host(mo_id, validate_host_request_type)
        print("The response of OvfManagerApi->ovf_manager_validate_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OvfManagerApi->ovf_manager_validate_host: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **validate_host_request_type** | [**ValidateHostRequestType**](ValidateHostRequestType.md)|  | 

### Return type

[**OvfValidateHostResult**](OvfValidateHostResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ValidateResult instance containing any warnings and/or errors from the validation.  |  -  |
**500** | ***TaskInProgress***: if a required managed entity is busy.  ***ConcurrentAccess***: if a concurrency issue prevents the operation from succeeding.  ***FileFault***: if there is a generic file error  ***InvalidState***: if the operation failed due to the current state of the system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

