# vmware_vi.CustomizationSpecManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customization_spec_manager_check_customization_resources**](CustomizationSpecManagerApi.md#customization_spec_manager_check_customization_resources) | **POST** /CustomizationSpecManager/{moId}/CheckCustomizationResources | Validate that required resources are available on the server to customize a particular guest operating system. 
[**customization_spec_manager_create_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_create_customization_spec) | **POST** /CustomizationSpecManager/{moId}/CreateCustomizationSpec | Creates a new specification. 
[**customization_spec_manager_customization_spec_item_to_xml**](CustomizationSpecManagerApi.md#customization_spec_manager_customization_spec_item_to_xml) | **POST** /CustomizationSpecManager/{moId}/CustomizationSpecItemToXml | Converts a specification item to XML text 
[**customization_spec_manager_delete_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_delete_customization_spec) | **POST** /CustomizationSpecManager/{moId}/DeleteCustomizationSpec | Deletes a specification. 
[**customization_spec_manager_does_customization_spec_exist**](CustomizationSpecManagerApi.md#customization_spec_manager_does_customization_spec_exist) | **POST** /CustomizationSpecManager/{moId}/DoesCustomizationSpecExist | Whether or not a specification exists. 
[**customization_spec_manager_duplicate_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_duplicate_customization_spec) | **POST** /CustomizationSpecManager/{moId}/DuplicateCustomizationSpec | Duplicates a specification. 
[**customization_spec_manager_get_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_get_customization_spec) | **POST** /CustomizationSpecManager/{moId}/GetCustomizationSpec | Obtains a specification for the given name. 
[**customization_spec_manager_get_encryption_key**](CustomizationSpecManagerApi.md#customization_spec_manager_get_encryption_key) | **GET** /CustomizationSpecManager/{moId}/encryptionKey | Gets a binary public encryption key that can be used to encrypt passwords in stored specifications. 
[**customization_spec_manager_get_info**](CustomizationSpecManagerApi.md#customization_spec_manager_get_info) | **GET** /CustomizationSpecManager/{moId}/info | Gets a list of information on available specifications. 
[**customization_spec_manager_overwrite_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_overwrite_customization_spec) | **POST** /CustomizationSpecManager/{moId}/OverwriteCustomizationSpec | Overwrites an existing specification, possibly after retrieving (by using &#39;get&#39;) and editing it. 
[**customization_spec_manager_rename_customization_spec**](CustomizationSpecManagerApi.md#customization_spec_manager_rename_customization_spec) | **POST** /CustomizationSpecManager/{moId}/RenameCustomizationSpec | Renames a specification. 
[**customization_spec_manager_xml_to_customization_spec_item**](CustomizationSpecManagerApi.md#customization_spec_manager_xml_to_customization_spec_item) | **POST** /CustomizationSpecManager/{moId}/XmlToCustomizationSpecItem | Converts an XML string to a specification item 


# **customization_spec_manager_check_customization_resources**
> customization_spec_manager_check_customization_resources(mo_id, check_customization_resources_request_type)

Validate that required resources are available on the server to customize a particular guest operating system. 

Validate that required resources are available on the server to customize a particular guest operating system.  These would include sysprep for Windows and the debugfs and changefs volume editors for Linux guests.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_customization_resources_request_type import CheckCustomizationResourcesRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_customization_resources_request_type = vmware_vi.CheckCustomizationResourcesRequestType() # CheckCustomizationResourcesRequestType | 

    try:
        # Validate that required resources are available on the server to customize a particular guest operating system. 
        api_instance.customization_spec_manager_check_customization_resources(mo_id, check_customization_resources_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_check_customization_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_customization_resources_request_type** | [**CheckCustomizationResourcesRequestType**](CheckCustomizationResourcesRequestType.md)|  | 

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
**500** | ***MissingLinuxCustResources***:   ***MissingWindowsCustResources***:   ***UncustomizableGuest***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_create_customization_spec**
> customization_spec_manager_create_customization_spec(mo_id, create_customization_spec_request_type)

Creates a new specification. 

Creates a new specification.  ***Required privileges:*** VirtualMachine.Provisioning.ModifyCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_customization_spec_request_type import CreateCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_customization_spec_request_type = vmware_vi.CreateCustomizationSpecRequestType() # CreateCustomizationSpecRequestType | 

    try:
        # Creates a new specification. 
        api_instance.customization_spec_manager_create_customization_spec(mo_id, create_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_create_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_customization_spec_request_type** | [**CreateCustomizationSpecRequestType**](CreateCustomizationSpecRequestType.md)|  | 

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
**500** | ***AlreadyExists***:   ***CannotDecryptPasswords***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_customization_spec_item_to_xml**
> str customization_spec_manager_customization_spec_item_to_xml(mo_id, customization_spec_item_to_xml_request_type)

Converts a specification item to XML text 

Converts a specification item to XML text  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customization_spec_item_to_xml_request_type import CustomizationSpecItemToXmlRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    customization_spec_item_to_xml_request_type = vmware_vi.CustomizationSpecItemToXmlRequestType() # CustomizationSpecItemToXmlRequestType | 

    try:
        # Converts a specification item to XML text 
        api_response = api_instance.customization_spec_manager_customization_spec_item_to_xml(mo_id, customization_spec_item_to_xml_request_type)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_customization_spec_item_to_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_customization_spec_item_to_xml: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **customization_spec_item_to_xml_request_type** | [**CustomizationSpecItemToXmlRequestType**](CustomizationSpecItemToXmlRequestType.md)|  | 

### Return type

**str**

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

# **customization_spec_manager_delete_customization_spec**
> customization_spec_manager_delete_customization_spec(mo_id, delete_customization_spec_request_type)

Deletes a specification. 

Deletes a specification.  ***Required privileges:*** VirtualMachine.Provisioning.ModifyCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_customization_spec_request_type import DeleteCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_customization_spec_request_type = vmware_vi.DeleteCustomizationSpecRequestType() # DeleteCustomizationSpecRequestType | 

    try:
        # Deletes a specification. 
        api_instance.customization_spec_manager_delete_customization_spec(mo_id, delete_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_delete_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_customization_spec_request_type** | [**DeleteCustomizationSpecRequestType**](DeleteCustomizationSpecRequestType.md)|  | 

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
**500** | ***NotFound***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_does_customization_spec_exist**
> bool customization_spec_manager_does_customization_spec_exist(mo_id, does_customization_spec_exist_request_type)

Whether or not a specification exists. 

Whether or not a specification exists.  ***Required privileges:*** VirtualMachine.Provisioning.ReadCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.does_customization_spec_exist_request_type import DoesCustomizationSpecExistRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    does_customization_spec_exist_request_type = vmware_vi.DoesCustomizationSpecExistRequestType() # DoesCustomizationSpecExistRequestType | 

    try:
        # Whether or not a specification exists. 
        api_response = api_instance.customization_spec_manager_does_customization_spec_exist(mo_id, does_customization_spec_exist_request_type)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_does_customization_spec_exist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_does_customization_spec_exist: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **does_customization_spec_exist_request_type** | [**DoesCustomizationSpecExistRequestType**](DoesCustomizationSpecExistRequestType.md)|  | 

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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_duplicate_customization_spec**
> customization_spec_manager_duplicate_customization_spec(mo_id, duplicate_customization_spec_request_type)

Duplicates a specification. 

Duplicates a specification.  ***Required privileges:*** VirtualMachine.Provisioning.ModifyCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.duplicate_customization_spec_request_type import DuplicateCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    duplicate_customization_spec_request_type = vmware_vi.DuplicateCustomizationSpecRequestType() # DuplicateCustomizationSpecRequestType | 

    try:
        # Duplicates a specification. 
        api_instance.customization_spec_manager_duplicate_customization_spec(mo_id, duplicate_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_duplicate_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **duplicate_customization_spec_request_type** | [**DuplicateCustomizationSpecRequestType**](DuplicateCustomizationSpecRequestType.md)|  | 

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
**500** | ***NotFound***:   ***AlreadyExists***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_get_customization_spec**
> CustomizationSpecItem customization_spec_manager_get_customization_spec(mo_id, get_customization_spec_request_type)

Obtains a specification for the given name. 

Obtains a specification for the given name.  ***Required privileges:*** VirtualMachine.Provisioning.ReadCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customization_spec_item import CustomizationSpecItem
from vmware_vi.models.get_customization_spec_request_type import GetCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_customization_spec_request_type = vmware_vi.GetCustomizationSpecRequestType() # GetCustomizationSpecRequestType | 

    try:
        # Obtains a specification for the given name. 
        api_response = api_instance.customization_spec_manager_get_customization_spec(mo_id, get_customization_spec_request_type)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_get_customization_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_get_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_customization_spec_request_type** | [**GetCustomizationSpecRequestType**](GetCustomizationSpecRequestType.md)|  | 

### Return type

[**CustomizationSpecItem**](CustomizationSpecItem.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotFound***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_get_encryption_key**
> List[int] customization_spec_manager_get_encryption_key(mo_id)

Gets a binary public encryption key that can be used to encrypt passwords in stored specifications. 

Gets a binary public encryption key that can be used to encrypt passwords in stored specifications.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Gets a binary public encryption key that can be used to encrypt passwords in stored specifications. 
        api_response = api_instance.customization_spec_manager_get_encryption_key(mo_id)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_get_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_get_encryption_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[int]**

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

# **customization_spec_manager_get_info**
> List[CustomizationSpecInfo] customization_spec_manager_get_info(mo_id)

Gets a list of information on available specifications. 

Gets a list of information on available specifications.  ***Required privileges:*** VirtualMachine.Provisioning.ReadCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customization_spec_info import CustomizationSpecInfo
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Gets a list of information on available specifications. 
        api_response = api_instance.customization_spec_manager_get_info(mo_id)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomizationSpecInfo]**](CustomizationSpecInfo.md)

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

# **customization_spec_manager_overwrite_customization_spec**
> customization_spec_manager_overwrite_customization_spec(mo_id, overwrite_customization_spec_request_type)

Overwrites an existing specification, possibly after retrieving (by using 'get') and editing it. 

Overwrites an existing specification, possibly after retrieving (by using 'get') and editing it.  If, based on the item's changeVersion value, the overwrite process detects that the specification has changed since its retrieval, then the API uses the SpecModified exception to warn clients that they might overwrite another client's change.  ***Required privileges:*** VirtualMachine.Provisioning.ModifyCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.overwrite_customization_spec_request_type import OverwriteCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    overwrite_customization_spec_request_type = vmware_vi.OverwriteCustomizationSpecRequestType() # OverwriteCustomizationSpecRequestType | 

    try:
        # Overwrites an existing specification, possibly after retrieving (by using 'get') and editing it. 
        api_instance.customization_spec_manager_overwrite_customization_spec(mo_id, overwrite_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_overwrite_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **overwrite_customization_spec_request_type** | [**OverwriteCustomizationSpecRequestType**](OverwriteCustomizationSpecRequestType.md)|  | 

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
**500** | ***NotFound***:   ***ConcurrentAccess***:   ***CannotDecryptPasswords***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_rename_customization_spec**
> customization_spec_manager_rename_customization_spec(mo_id, rename_customization_spec_request_type)

Renames a specification. 

Renames a specification.  ***Required privileges:*** VirtualMachine.Provisioning.ModifyCustSpecs 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.rename_customization_spec_request_type import RenameCustomizationSpecRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_customization_spec_request_type = vmware_vi.RenameCustomizationSpecRequestType() # RenameCustomizationSpecRequestType | 

    try:
        # Renames a specification. 
        api_instance.customization_spec_manager_rename_customization_spec(mo_id, rename_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_rename_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_customization_spec_request_type** | [**RenameCustomizationSpecRequestType**](RenameCustomizationSpecRequestType.md)|  | 

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
**500** | ***NotFound***:   ***AlreadyExists***:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customization_spec_manager_xml_to_customization_spec_item**
> CustomizationSpecItem customization_spec_manager_xml_to_customization_spec_item(mo_id, xml_to_customization_spec_item_request_type)

Converts an XML string to a specification item 

Converts an XML string to a specification item  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customization_spec_item import CustomizationSpecItem
from vmware_vi.models.xml_to_customization_spec_item_request_type import XmlToCustomizationSpecItemRequestType
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
    api_instance = vmware_vi.CustomizationSpecManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    xml_to_customization_spec_item_request_type = vmware_vi.XmlToCustomizationSpecItemRequestType() # XmlToCustomizationSpecItemRequestType | 

    try:
        # Converts an XML string to a specification item 
        api_response = api_instance.customization_spec_manager_xml_to_customization_spec_item(mo_id, xml_to_customization_spec_item_request_type)
        print("The response of CustomizationSpecManagerApi->customization_spec_manager_xml_to_customization_spec_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationSpecManagerApi->customization_spec_manager_xml_to_customization_spec_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **xml_to_customization_spec_item_request_type** | [**XmlToCustomizationSpecItemRequestType**](XmlToCustomizationSpecItemRequestType.md)|  | 

### Return type

[**CustomizationSpecItem**](CustomizationSpecItem.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

