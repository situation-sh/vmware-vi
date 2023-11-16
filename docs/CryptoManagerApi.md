# vmware_vi.CryptoManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_manager_add_key**](CryptoManagerApi.md#crypto_manager_add_key) | **POST** /CryptoManager/{moId}/AddKey | Add an existing key. 
[**crypto_manager_add_keys**](CryptoManagerApi.md#crypto_manager_add_keys) | **POST** /CryptoManager/{moId}/AddKeys | Add multiple existing keys. 
[**crypto_manager_get_enabled**](CryptoManagerApi.md#crypto_manager_get_enabled) | **GET** /CryptoManager/{moId}/enabled | Indicate if the encryption feature is enabled. 
[**crypto_manager_list_keys**](CryptoManagerApi.md#crypto_manager_list_keys) | **POST** /CryptoManager/{moId}/ListKeys | List keys. 
[**crypto_manager_remove_key**](CryptoManagerApi.md#crypto_manager_remove_key) | **POST** /CryptoManager/{moId}/RemoveKey | Remove a key (only the UUID is needed to remove). 
[**crypto_manager_remove_keys**](CryptoManagerApi.md#crypto_manager_remove_keys) | **POST** /CryptoManager/{moId}/RemoveKeys | Remove multiple keys (only the UUID is needed to remove). 


# **crypto_manager_add_key**
> crypto_manager_add_key(mo_id, add_key_request_type)

Add an existing key. 

Add an existing key.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_key_request_type import AddKeyRequestType
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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_key_request_type = vmware_vi.AddKeyRequestType() # AddKeyRequestType | 

    try:
        # Add an existing key. 
        api_instance.crypto_manager_add_key(mo_id, add_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_add_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_key_request_type** | [**AddKeyRequestType**](AddKeyRequestType.md)|  | 

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
**500** | ***AlreadyExists***: in case the key is already in the key cache  ***InvalidState***: in case the host is not Crypto Safe  ***InvalidArgument***: in case the keyID is duplicated or key properties are incorrect.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_add_keys**
> List[CryptoKeyResult] crypto_manager_add_keys(mo_id, add_keys_request_type)

Add multiple existing keys. 

Add multiple existing keys.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_keys_request_type import AddKeysRequestType
from vmware_vi.models.crypto_key_result import CryptoKeyResult
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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_keys_request_type = vmware_vi.AddKeysRequestType() # AddKeysRequestType | 

    try:
        # Add multiple existing keys. 
        api_response = api_instance.crypto_manager_add_keys(mo_id, add_keys_request_type)
        print("The response of CryptoManagerApi->crypto_manager_add_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_add_keys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_keys_request_type** | [**AddKeysRequestType**](AddKeysRequestType.md)|  | 

### Return type

[**List[CryptoKeyResult]**](CryptoKeyResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the result for each key operation.  |  -  |
**500** | ***InvalidState***: in case the host is not Crypto Safe  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_get_enabled**
> bool crypto_manager_get_enabled(mo_id)

Indicate if the encryption feature is enabled. 

Indicate if the encryption feature is enabled.  ***Since:*** vSphere API 6.5 

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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Indicate if the encryption feature is enabled. 
        api_response = api_instance.crypto_manager_get_enabled(mo_id)
        print("The response of CryptoManagerApi->crypto_manager_get_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_get_enabled: %s\n" % e)
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

# **crypto_manager_list_keys**
> List[CryptoKeyId] crypto_manager_list_keys(mo_id, list_keys_request_type)

List keys. 

List keys.  \\* When executed against the host, lists all the keys added to the host's key cache by *CryptoManager.AddKey*/*CryptoManager.AddKeys*. \\* When executed against the VC, lists all the keys used by the correctly registered VMs, and the host key.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_key_id import CryptoKeyId
from vmware_vi.models.list_keys_request_type import ListKeysRequestType
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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_keys_request_type = vmware_vi.ListKeysRequestType() # ListKeysRequestType | 

    try:
        # List keys. 
        api_response = api_instance.crypto_manager_list_keys(mo_id, list_keys_request_type)
        print("The response of CryptoManagerApi->crypto_manager_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_list_keys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_keys_request_type** | [**ListKeysRequestType**](ListKeysRequestType.md)|  | 

### Return type

[**List[CryptoKeyId]**](CryptoKeyId.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of known keys.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_remove_key**
> crypto_manager_remove_key(mo_id, remove_key_request_type)

Remove a key (only the UUID is needed to remove). 

Remove a key (only the UUID is needed to remove).  If \"force\" is set, removal will happen even if the key is in use.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_key_request_type import RemoveKeyRequestType
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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_key_request_type = vmware_vi.RemoveKeyRequestType() # RemoveKeyRequestType | 

    try:
        # Remove a key (only the UUID is needed to remove). 
        api_instance.crypto_manager_remove_key(mo_id, remove_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_remove_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_key_request_type** | [**RemoveKeyRequestType**](RemoveKeyRequestType.md)|  | 

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
**500** | ***InvalidArgument***: in case the keyID is not found and \&quot;force\&quot; is false.  ***ResourceInUse***: if the key is used to encrypt any object and \&quot;force\&quot; is false.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_remove_keys**
> List[CryptoKeyResult] crypto_manager_remove_keys(mo_id, remove_keys_request_type)

Remove multiple keys (only the UUID is needed to remove). 

Remove multiple keys (only the UUID is needed to remove).  If \"force\" is set, removal will happen even if they are in use.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_key_result import CryptoKeyResult
from vmware_vi.models.remove_keys_request_type import RemoveKeysRequestType
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
    api_instance = vmware_vi.CryptoManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_keys_request_type = vmware_vi.RemoveKeysRequestType() # RemoveKeysRequestType | 

    try:
        # Remove multiple keys (only the UUID is needed to remove). 
        api_response = api_instance.crypto_manager_remove_keys(mo_id, remove_keys_request_type)
        print("The response of CryptoManagerApi->crypto_manager_remove_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerApi->crypto_manager_remove_keys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_keys_request_type** | [**RemoveKeysRequestType**](RemoveKeysRequestType.md)|  | 

### Return type

[**List[CryptoKeyResult]**](CryptoKeyResult.md)

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

