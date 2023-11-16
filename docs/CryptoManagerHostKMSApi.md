# vmware_vi.CryptoManagerHostKMSApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_manager_host_kms_add_key**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_add_key) | **POST** /CryptoManagerHostKMS/{moId}/AddKey | Add an existing key. 
[**crypto_manager_host_kms_add_keys**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_add_keys) | **POST** /CryptoManagerHostKMS/{moId}/AddKeys | Add multiple existing keys. 
[**crypto_manager_host_kms_change_key_task**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_change_key_task) | **POST** /CryptoManagerHostKMS/{moId}/ChangeKey_Task | Change the key used for core dump encryption Note: *CryptoManagerHost.CryptoManagerHostEnable* must be called first If successful, a \&quot;best effort\&quot; will be made to \&quot;in place\&quot; shallow recrypt any core dumps found in /var/core to use the new key. 
[**crypto_manager_host_kms_crypto_manager_host_disable**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_crypto_manager_host_disable) | **POST** /CryptoManagerHostKMS/{moId}/CryptoManagerHostDisable | Disable encryption on host, if host was in crypto safe mode, put it in pendingIncapable state and host will be crypto incapable after a reboot Note: A reboot is expected from user after successfully invoking this API Note: Do not call this API if the host is in vSAN encrypted cluster 
[**crypto_manager_host_kms_crypto_manager_host_enable**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_crypto_manager_host_enable) | **POST** /CryptoManagerHostKMS/{moId}/CryptoManagerHostEnable | Begin core dump encryption by specifying the encryption key and put the host in *safe* state Note: *CryptoManagerHost.CryptoManagerHostPrepare* must be called first 
[**crypto_manager_host_kms_crypto_manager_host_prepare**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_crypto_manager_host_prepare) | **POST** /CryptoManagerHostKMS/{moId}/CryptoManagerHostPrepare | Prime the host to receive sensitive information and put the host in *prepared* state 
[**crypto_manager_host_kms_get_crypto_key_status**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_get_crypto_key_status) | **POST** /CryptoManagerHostKMS/{moId}/GetCryptoKeyStatus | Get the key status on the host. 
[**crypto_manager_host_kms_get_enabled**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_get_enabled) | **GET** /CryptoManagerHostKMS/{moId}/enabled | Indicate if the encryption feature is enabled. 
[**crypto_manager_host_kms_list_keys**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_list_keys) | **POST** /CryptoManagerHostKMS/{moId}/ListKeys | List keys. 
[**crypto_manager_host_kms_remove_key**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_remove_key) | **POST** /CryptoManagerHostKMS/{moId}/RemoveKey | Remove a key (only the UUID is needed to remove). 
[**crypto_manager_host_kms_remove_keys**](CryptoManagerHostKMSApi.md#crypto_manager_host_kms_remove_keys) | **POST** /CryptoManagerHostKMS/{moId}/RemoveKeys | Remove multiple keys (only the UUID is needed to remove). 


# **crypto_manager_host_kms_add_key**
> crypto_manager_host_kms_add_key(mo_id, add_key_request_type)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_key_request_type = vmware_vi.AddKeyRequestType() # AddKeyRequestType | 

    try:
        # Add an existing key. 
        api_instance.crypto_manager_host_kms_add_key(mo_id, add_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_add_key: %s\n" % e)
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

# **crypto_manager_host_kms_add_keys**
> List[CryptoKeyResult] crypto_manager_host_kms_add_keys(mo_id, add_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_keys_request_type = vmware_vi.AddKeysRequestType() # AddKeysRequestType | 

    try:
        # Add multiple existing keys. 
        api_response = api_instance.crypto_manager_host_kms_add_keys(mo_id, add_keys_request_type)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_add_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_add_keys: %s\n" % e)
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

# **crypto_manager_host_kms_change_key_task**
> ManagedObjectReference crypto_manager_host_kms_change_key_task(mo_id, change_key_request_type)

Change the key used for core dump encryption Note: *CryptoManagerHost.CryptoManagerHostEnable* must be called first If successful, a \"best effort\" will be made to \"in place\" shallow recrypt any core dumps found in /var/core to use the new key. 

Change the key used for core dump encryption Note: *CryptoManagerHost.CryptoManagerHostEnable* must be called first If successful, a \"best effort\" will be made to \"in place\" shallow recrypt any core dumps found in /var/core to use the new key.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Cryptographer.RegisterHost 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_key_request_type import ChangeKeyRequestType
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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_key_request_type = vmware_vi.ChangeKeyRequestType() # ChangeKeyRequestType | 

    try:
        # Change the key used for core dump encryption Note: *CryptoManagerHost.CryptoManagerHostEnable* must be called first If successful, a \"best effort\" will be made to \"in place\" shallow recrypt any core dumps found in /var/core to use the new key. 
        api_response = api_instance.crypto_manager_host_kms_change_key_task(mo_id, change_key_request_type)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_change_key_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_change_key_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_key_request_type** | [**ChangeKeyRequestType**](ChangeKeyRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: if the host is not in *safe* state  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_host_kms_crypto_manager_host_disable**
> crypto_manager_host_kms_crypto_manager_host_disable(mo_id)

Disable encryption on host, if host was in crypto safe mode, put it in pendingIncapable state and host will be crypto incapable after a reboot Note: A reboot is expected from user after successfully invoking this API Note: Do not call this API if the host is in vSAN encrypted cluster 

Disable encryption on host, if host was in crypto safe mode, put it in pendingIncapable state and host will be crypto incapable after a reboot Note: A reboot is expected from user after successfully invoking this API Note: Do not call this API if the host is in vSAN encrypted cluster  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.RegisterHost 

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Disable encryption on host, if host was in crypto safe mode, put it in pendingIncapable state and host will be crypto incapable after a reboot Note: A reboot is expected from user after successfully invoking this API Note: Do not call this API if the host is in vSAN encrypted cluster 
        api_instance.crypto_manager_host_kms_crypto_manager_host_disable(mo_id)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_crypto_manager_host_disable: %s\n" % e)
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
**500** | ***InvalidState***: if the host is already crypto disabled.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_host_kms_crypto_manager_host_enable**
> crypto_manager_host_kms_crypto_manager_host_enable(mo_id, crypto_manager_host_enable_request_type)

Begin core dump encryption by specifying the encryption key and put the host in *safe* state Note: *CryptoManagerHost.CryptoManagerHostPrepare* must be called first 

Begin core dump encryption by specifying the encryption key and put the host in *safe* state Note: *CryptoManagerHost.CryptoManagerHostPrepare* must be called first  ***Since:*** vSphere API 6.7  ***Required privileges:*** Cryptographer.RegisterHost 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_manager_host_enable_request_type import CryptoManagerHostEnableRequestType
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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    crypto_manager_host_enable_request_type = vmware_vi.CryptoManagerHostEnableRequestType() # CryptoManagerHostEnableRequestType | 

    try:
        # Begin core dump encryption by specifying the encryption key and put the host in *safe* state Note: *CryptoManagerHost.CryptoManagerHostPrepare* must be called first 
        api_instance.crypto_manager_host_kms_crypto_manager_host_enable(mo_id, crypto_manager_host_enable_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_crypto_manager_host_enable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **crypto_manager_host_enable_request_type** | [**CryptoManagerHostEnableRequestType**](CryptoManagerHostEnableRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host is in *incapable* state  ***AlreadyExists***: if the host is in *safe* state and initialKey differs from the existing core dump encryption key  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_host_kms_crypto_manager_host_prepare**
> crypto_manager_host_kms_crypto_manager_host_prepare(mo_id)

Prime the host to receive sensitive information and put the host in *prepared* state 

Prime the host to receive sensitive information and put the host in *prepared* state  ***Since:*** vSphere API 6.7  ***Required privileges:*** Cryptographer.RegisterHost 

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Prime the host to receive sensitive information and put the host in *prepared* state 
        api_instance.crypto_manager_host_kms_crypto_manager_host_prepare(mo_id)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_crypto_manager_host_prepare: %s\n" % e)
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
**500** | ***InvalidState***: if the host is not in *incapable* state  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_host_kms_get_crypto_key_status**
> List[CryptoManagerHostKeyStatus] crypto_manager_host_kms_get_crypto_key_status(mo_id, get_crypto_key_status_request_type)

Get the key status on the host. 

Get the key status on the host.  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_manager_host_key_status import CryptoManagerHostKeyStatus
from vmware_vi.models.get_crypto_key_status_request_type import GetCryptoKeyStatusRequestType
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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_crypto_key_status_request_type = vmware_vi.GetCryptoKeyStatusRequestType() # GetCryptoKeyStatusRequestType | 

    try:
        # Get the key status on the host. 
        api_response = api_instance.crypto_manager_host_kms_get_crypto_key_status(mo_id, get_crypto_key_status_request_type)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_get_crypto_key_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_get_crypto_key_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_crypto_key_status_request_type** | [**GetCryptoKeyStatusRequestType**](GetCryptoKeyStatusRequestType.md)|  | 

### Return type

[**List[CryptoManagerHostKeyStatus]**](CryptoManagerHostKeyStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the key status.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_host_kms_get_enabled**
> bool crypto_manager_host_kms_get_enabled(mo_id)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Indicate if the encryption feature is enabled. 
        api_response = api_instance.crypto_manager_host_kms_get_enabled(mo_id)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_get_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_get_enabled: %s\n" % e)
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

# **crypto_manager_host_kms_list_keys**
> List[CryptoKeyId] crypto_manager_host_kms_list_keys(mo_id, list_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_keys_request_type = vmware_vi.ListKeysRequestType() # ListKeysRequestType | 

    try:
        # List keys. 
        api_response = api_instance.crypto_manager_host_kms_list_keys(mo_id, list_keys_request_type)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_list_keys: %s\n" % e)
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

# **crypto_manager_host_kms_remove_key**
> crypto_manager_host_kms_remove_key(mo_id, remove_key_request_type)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_key_request_type = vmware_vi.RemoveKeyRequestType() # RemoveKeyRequestType | 

    try:
        # Remove a key (only the UUID is needed to remove). 
        api_instance.crypto_manager_host_kms_remove_key(mo_id, remove_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_remove_key: %s\n" % e)
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

# **crypto_manager_host_kms_remove_keys**
> List[CryptoKeyResult] crypto_manager_host_kms_remove_keys(mo_id, remove_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerHostKMSApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_keys_request_type = vmware_vi.RemoveKeysRequestType() # RemoveKeysRequestType | 

    try:
        # Remove multiple keys (only the UUID is needed to remove). 
        api_response = api_instance.crypto_manager_host_kms_remove_keys(mo_id, remove_keys_request_type)
        print("The response of CryptoManagerHostKMSApi->crypto_manager_host_kms_remove_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerHostKMSApi->crypto_manager_host_kms_remove_keys: %s\n" % e)
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

