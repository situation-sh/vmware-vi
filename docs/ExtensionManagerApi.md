# vmware_vi.ExtensionManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extension_manager_find_extension**](ExtensionManagerApi.md#extension_manager_find_extension) | **POST** /ExtensionManager/{moId}/FindExtension | Returns extension with the given key, if any. 
[**extension_manager_get_extension_list**](ExtensionManagerApi.md#extension_manager_get_extension_list) | **GET** /ExtensionManager/{moId}/extensionList | The list of currently registered extensions. 
[**extension_manager_get_public_key**](ExtensionManagerApi.md#extension_manager_get_public_key) | **POST** /ExtensionManager/{moId}/GetPublicKey | Returns VirtualCenter Server public key. 
[**extension_manager_query_extension_ip_allocation_usage**](ExtensionManagerApi.md#extension_manager_query_extension_ip_allocation_usage) | **POST** /ExtensionManager/{moId}/QueryExtensionIpAllocationUsage | Query statistics about IP allocation usage, either system wide or for specified extensions. 
[**extension_manager_query_managed_by**](ExtensionManagerApi.md#extension_manager_query_managed_by) | **POST** /ExtensionManager/{moId}/QueryManagedBy | Find entities managed by an extension. 
[**extension_manager_register_extension**](ExtensionManagerApi.md#extension_manager_register_extension) | **POST** /ExtensionManager/{moId}/RegisterExtension | Registers extension. 
[**extension_manager_set_extension_certificate**](ExtensionManagerApi.md#extension_manager_set_extension_certificate) | **POST** /ExtensionManager/{moId}/SetExtensionCertificate | Update the stored authentication certificate for a specified extension. 
[**extension_manager_set_public_key**](ExtensionManagerApi.md#extension_manager_set_public_key) | **POST** /ExtensionManager/{moId}/SetPublicKey | Sets extension&#39;s public key. 
[**extension_manager_unregister_extension**](ExtensionManagerApi.md#extension_manager_unregister_extension) | **POST** /ExtensionManager/{moId}/UnregisterExtension | Unregisters the specified extension if it exists. 
[**extension_manager_update_extension**](ExtensionManagerApi.md#extension_manager_update_extension) | **POST** /ExtensionManager/{moId}/UpdateExtension | If the key specified in the extension exists, the existing record is updated. 


# **extension_manager_find_extension**
> Extension extension_manager_find_extension(mo_id, find_extension_request_type)

Returns extension with the given key, if any. 

Returns extension with the given key, if any.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extension import Extension
from vmware_vi.models.find_extension_request_type import FindExtensionRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_extension_request_type = vmware_vi.FindExtensionRequestType() # FindExtensionRequestType | 

    try:
        # Returns extension with the given key, if any. 
        api_response = api_instance.extension_manager_find_extension(mo_id, find_extension_request_type)
        print("The response of ExtensionManagerApi->extension_manager_find_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_find_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_extension_request_type** | [**FindExtensionRequestType**](FindExtensionRequestType.md)|  | 

### Return type

[**Extension**](Extension.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extension that matches given key, if any.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_get_extension_list**
> List[Extension] extension_manager_get_extension_list(mo_id)

The list of currently registered extensions. 

The list of currently registered extensions.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extension import Extension
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of currently registered extensions. 
        api_response = api_instance.extension_manager_get_extension_list(mo_id)
        print("The response of ExtensionManagerApi->extension_manager_get_extension_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_get_extension_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Extension]**](Extension.md)

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

# **extension_manager_get_public_key**
> str extension_manager_get_public_key(mo_id)

Returns VirtualCenter Server public key. 

Deprecated as of VI 4.0, use trusted certificates and *SessionManager.LoginExtensionBySubjectName* or *ExtensionManager.SetExtensionCertificate* and *SessionManager.LoginExtensionByCertificate*.  Returns VirtualCenter Server public key.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns VirtualCenter Server public key. 
        api_response = api_instance.extension_manager_get_public_key(mo_id)
        print("The response of ExtensionManagerApi->extension_manager_get_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_get_public_key: %s\n" % e)
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
**200** | Public key of VirtualCenter Server, encoded in PEM (privacy-enhanced mail) format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_query_extension_ip_allocation_usage**
> List[ExtensionManagerIpAllocationUsage] extension_manager_query_extension_ip_allocation_usage(mo_id, query_extension_ip_allocation_usage_request_type)

Query statistics about IP allocation usage, either system wide or for specified extensions. 

Query statistics about IP allocation usage, either system wide or for specified extensions.  Refer to *IpPoolManager* for details.  ***Since:*** vSphere API 5.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extension_manager_ip_allocation_usage import ExtensionManagerIpAllocationUsage
from vmware_vi.models.query_extension_ip_allocation_usage_request_type import QueryExtensionIpAllocationUsageRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_extension_ip_allocation_usage_request_type = vmware_vi.QueryExtensionIpAllocationUsageRequestType() # QueryExtensionIpAllocationUsageRequestType | 

    try:
        # Query statistics about IP allocation usage, either system wide or for specified extensions. 
        api_response = api_instance.extension_manager_query_extension_ip_allocation_usage(mo_id, query_extension_ip_allocation_usage_request_type)
        print("The response of ExtensionManagerApi->extension_manager_query_extension_ip_allocation_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_query_extension_ip_allocation_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_extension_ip_allocation_usage_request_type** | [**QueryExtensionIpAllocationUsageRequestType**](QueryExtensionIpAllocationUsageRequestType.md)|  | 

### Return type

[**List[ExtensionManagerIpAllocationUsage]**](ExtensionManagerIpAllocationUsage.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of IP allocation usage.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_query_managed_by**
> List[ManagedObjectReference] extension_manager_query_managed_by(mo_id, query_managed_by_request_type)

Find entities managed by an extension. 

Find entities managed by an extension.  These can be either virtual machines or vApps.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_managed_by_request_type import QueryManagedByRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_managed_by_request_type = vmware_vi.QueryManagedByRequestType() # QueryManagedByRequestType | 

    try:
        # Find entities managed by an extension. 
        api_response = api_instance.extension_manager_query_managed_by(mo_id, query_managed_by_request_type)
        print("The response of ExtensionManagerApi->extension_manager_query_managed_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_query_managed_by: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_managed_by_request_type** | [**QueryManagedByRequestType**](QueryManagedByRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entities managed by the extension.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_register_extension**
> extension_manager_register_extension(mo_id, register_extension_request_type)

Registers extension. 

Registers extension.  ***Since:*** VI API 2.5  ***Required privileges:*** Extension.Register 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.register_extension_request_type import RegisterExtensionRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_extension_request_type = vmware_vi.RegisterExtensionRequestType() # RegisterExtensionRequestType | 

    try:
        # Registers extension. 
        api_instance.extension_manager_register_extension(mo_id, register_extension_request_type)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_register_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_extension_request_type** | [**RegisterExtensionRequestType**](RegisterExtensionRequestType.md)|  | 

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

# **extension_manager_set_extension_certificate**
> extension_manager_set_extension_certificate(mo_id, set_extension_certificate_request_type)

Update the stored authentication certificate for a specified extension. 

Update the stored authentication certificate for a specified extension.  Updates the registration of the specified extension with the thumbprint of the X.509 client certificate provided over SSL handshake, or by the &quot;certificatePem&quot;argument. The thumbprint will be used to authenticate the extension during invocations of *SessionManager.LoginExtensionByCertificate*.  NOTE: No verification is performed on the received certificate, such as expiry or revocation.  This method will unset any public key or subject name associated with the extension.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Extension.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_extension_certificate_request_type import SetExtensionCertificateRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_extension_certificate_request_type = vmware_vi.SetExtensionCertificateRequestType() # SetExtensionCertificateRequestType | 

    try:
        # Update the stored authentication certificate for a specified extension. 
        api_instance.extension_manager_set_extension_certificate(mo_id, set_extension_certificate_request_type)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_set_extension_certificate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_extension_certificate_request_type** | [**SetExtensionCertificateRequestType**](SetExtensionCertificateRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if the certificate described by &amp;quot;certificatePem&amp;quot; is not in PEM format, or could not be decoded to an X.509 certificate.  ***NoClientCertificate***: if certificatePem is not specified, and no certificate was passed over SSL handshake.  ***NotFound***: if an extension specified by &amp;quot;extensionKey&amp;quot; is not registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_set_public_key**
> extension_manager_set_public_key(mo_id, set_public_key_request_type)

Sets extension's public key. 

Deprecated as of VI 4.0, use trusted certificates and *SessionManager.LoginExtensionBySubjectName* or *ExtensionManager.SetExtensionCertificate* and *SessionManager.LoginExtensionByCertificate*.  Sets extension's public key.  This method will unset any subject name or certificate associated with the extension.  ***Since:*** VI API 2.5  ***Required privileges:*** Extension.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_public_key_request_type import SetPublicKeyRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_public_key_request_type = vmware_vi.SetPublicKeyRequestType() # SetPublicKeyRequestType | 

    try:
        # Sets extension's public key. 
        api_instance.extension_manager_set_public_key(mo_id, set_public_key_request_type)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_set_public_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_public_key_request_type** | [**SetPublicKeyRequestType**](SetPublicKeyRequestType.md)|  | 

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

# **extension_manager_unregister_extension**
> extension_manager_unregister_extension(mo_id, unregister_extension_request_type)

Unregisters the specified extension if it exists. 

Unregisters the specified extension if it exists.  ***Since:*** VI API 2.5  ***Required privileges:*** Extension.Unregister 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unregister_extension_request_type import UnregisterExtensionRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unregister_extension_request_type = vmware_vi.UnregisterExtensionRequestType() # UnregisterExtensionRequestType | 

    try:
        # Unregisters the specified extension if it exists. 
        api_instance.extension_manager_unregister_extension(mo_id, unregister_extension_request_type)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_unregister_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unregister_extension_request_type** | [**UnregisterExtensionRequestType**](UnregisterExtensionRequestType.md)|  | 

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
**500** | ***NotFound***: if the specified extension is not registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_manager_update_extension**
> extension_manager_update_extension(mo_id, update_extension_request_type)

If the key specified in the extension exists, the existing record is updated. 

If the key specified in the extension exists, the existing record is updated.  If the &quot;subjectName&quot; property of the Extension object has a value, and it is different from the existing value, this method will unset any public key or certificate associated with the extension.  ***Since:*** VI API 2.5  ***Required privileges:*** Extension.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_extension_request_type import UpdateExtensionRequestType
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
    api_instance = vmware_vi.ExtensionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_extension_request_type = vmware_vi.UpdateExtensionRequestType() # UpdateExtensionRequestType | 

    try:
        # If the key specified in the extension exists, the existing record is updated. 
        api_instance.extension_manager_update_extension(mo_id, update_extension_request_type)
    except Exception as e:
        print("Exception when calling ExtensionManagerApi->extension_manager_update_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_extension_request_type** | [**UpdateExtensionRequestType**](UpdateExtensionRequestType.md)|  | 

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
**500** | ***NotFound***: if the specified extension key is not registered.  ***InvalidArgument***: if the Extension description is incomplete or invalid, or if the extension is an OVF extension and its section types overlap with other registered OVF extensions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

