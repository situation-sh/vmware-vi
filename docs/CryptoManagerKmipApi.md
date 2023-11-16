# vmware_vi.CryptoManagerKmipApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_manager_kmip_add_key**](CryptoManagerKmipApi.md#crypto_manager_kmip_add_key) | **POST** /CryptoManagerKmip/{moId}/AddKey | Add an existing key. 
[**crypto_manager_kmip_add_keys**](CryptoManagerKmipApi.md#crypto_manager_kmip_add_keys) | **POST** /CryptoManagerKmip/{moId}/AddKeys | Add multiple existing keys. 
[**crypto_manager_kmip_generate_client_csr**](CryptoManagerKmipApi.md#crypto_manager_kmip_generate_client_csr) | **POST** /CryptoManagerKmip/{moId}/GenerateClientCsr | Generate a certificate signing request with its private key. 
[**crypto_manager_kmip_generate_key**](CryptoManagerKmipApi.md#crypto_manager_kmip_generate_key) | **POST** /CryptoManagerKmip/{moId}/GenerateKey | Generate new encryption key. 
[**crypto_manager_kmip_generate_self_signed_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_generate_self_signed_client_cert) | **POST** /CryptoManagerKmip/{moId}/GenerateSelfSignedClientCert | Generate a self-signed client certificate with its private key. 
[**crypto_manager_kmip_get_default_kms_cluster**](CryptoManagerKmipApi.md#crypto_manager_kmip_get_default_kms_cluster) | **POST** /CryptoManagerKmip/{moId}/GetDefaultKmsCluster | Get the default KMS cluster of the specified managed entity. 
[**crypto_manager_kmip_get_enabled**](CryptoManagerKmipApi.md#crypto_manager_kmip_get_enabled) | **GET** /CryptoManagerKmip/{moId}/enabled | Indicate if the encryption feature is enabled. 
[**crypto_manager_kmip_get_kmip_servers**](CryptoManagerKmipApi.md#crypto_manager_kmip_get_kmip_servers) | **GET** /CryptoManagerKmip/{moId}/kmipServers | A list of registered KMIP servers, grouped by clusters. 
[**crypto_manager_kmip_is_kms_cluster_active**](CryptoManagerKmipApi.md#crypto_manager_kmip_is_kms_cluster_active) | **POST** /CryptoManagerKmip/{moId}/IsKmsClusterActive | Check whether an active KMS exists in cluster. 
[**crypto_manager_kmip_list_keys**](CryptoManagerKmipApi.md#crypto_manager_kmip_list_keys) | **POST** /CryptoManagerKmip/{moId}/ListKeys | List keys. 
[**crypto_manager_kmip_list_kmip_servers**](CryptoManagerKmipApi.md#crypto_manager_kmip_list_kmip_servers) | **POST** /CryptoManagerKmip/{moId}/ListKmipServers | List the registered KMIP servers. 
[**crypto_manager_kmip_list_kms_clusters**](CryptoManagerKmipApi.md#crypto_manager_kmip_list_kms_clusters) | **POST** /CryptoManagerKmip/{moId}/ListKmsClusters | List the KMS clusters information. 
[**crypto_manager_kmip_mark_default**](CryptoManagerKmipApi.md#crypto_manager_kmip_mark_default) | **POST** /CryptoManagerKmip/{moId}/MarkDefault | Set the default KMIP cluster. 
[**crypto_manager_kmip_query_crypto_key_status**](CryptoManagerKmipApi.md#crypto_manager_kmip_query_crypto_key_status) | **POST** /CryptoManagerKmip/{moId}/QueryCryptoKeyStatus | Check CryptoKey status, such as if VC can access the key, if the key is used by some VMs or as host key. 
[**crypto_manager_kmip_register_kmip_server**](CryptoManagerKmipApi.md#crypto_manager_kmip_register_kmip_server) | **POST** /CryptoManagerKmip/{moId}/RegisterKmipServer | Register a KMIP server. 
[**crypto_manager_kmip_register_kms_cluster**](CryptoManagerKmipApi.md#crypto_manager_kmip_register_kms_cluster) | **POST** /CryptoManagerKmip/{moId}/RegisterKmsCluster | Register the specified KMS cluster to the CryptoManager. 
[**crypto_manager_kmip_remove_key**](CryptoManagerKmipApi.md#crypto_manager_kmip_remove_key) | **POST** /CryptoManagerKmip/{moId}/RemoveKey | Remove a key (only the UUID is needed to remove). 
[**crypto_manager_kmip_remove_keys**](CryptoManagerKmipApi.md#crypto_manager_kmip_remove_keys) | **POST** /CryptoManagerKmip/{moId}/RemoveKeys | Remove multiple keys (only the UUID is needed to remove). 
[**crypto_manager_kmip_remove_kmip_server**](CryptoManagerKmipApi.md#crypto_manager_kmip_remove_kmip_server) | **POST** /CryptoManagerKmip/{moId}/RemoveKmipServer | Remove a KMIP server, even if in use. 
[**crypto_manager_kmip_retrieve_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_retrieve_client_cert) | **POST** /CryptoManagerKmip/{moId}/RetrieveClientCert | Get the client certificate of the KMIP cluster. 
[**crypto_manager_kmip_retrieve_client_csr**](CryptoManagerKmipApi.md#crypto_manager_kmip_retrieve_client_csr) | **POST** /CryptoManagerKmip/{moId}/RetrieveClientCsr | Get the generated client certificate signing request. 
[**crypto_manager_kmip_retrieve_kmip_server_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_retrieve_kmip_server_cert) | **POST** /CryptoManagerKmip/{moId}/RetrieveKmipServerCert | Get the server certficate. 
[**crypto_manager_kmip_retrieve_kmip_servers_status_task**](CryptoManagerKmipApi.md#crypto_manager_kmip_retrieve_kmip_servers_status_task) | **POST** /CryptoManagerKmip/{moId}/RetrieveKmipServersStatus_Task | Get the status of the KMIP servers. 
[**crypto_manager_kmip_retrieve_self_signed_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_retrieve_self_signed_client_cert) | **POST** /CryptoManagerKmip/{moId}/RetrieveSelfSignedClientCert | Get the generated self signed client certificate. 
[**crypto_manager_kmip_set_default_kms_cluster**](CryptoManagerKmipApi.md#crypto_manager_kmip_set_default_kms_cluster) | **POST** /CryptoManagerKmip/{moId}/SetDefaultKmsCluster | Set the default KMS cluster for the specified managed entity. 
[**crypto_manager_kmip_set_key_custom_attributes**](CryptoManagerKmipApi.md#crypto_manager_kmip_set_key_custom_attributes) | **POST** /CryptoManagerKmip/{moId}/SetKeyCustomAttributes | Set crypto key&#39;s custom attributes. 
[**crypto_manager_kmip_unregister_kms_cluster**](CryptoManagerKmipApi.md#crypto_manager_kmip_unregister_kms_cluster) | **POST** /CryptoManagerKmip/{moId}/UnregisterKmsCluster | Unregister the specified KMS cluster from the CryptoManager. 
[**crypto_manager_kmip_update_kmip_server**](CryptoManagerKmipApi.md#crypto_manager_kmip_update_kmip_server) | **POST** /CryptoManagerKmip/{moId}/UpdateKmipServer | Update a KMIP server. 
[**crypto_manager_kmip_update_kms_signed_csr_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_update_kms_signed_csr_client_cert) | **POST** /CryptoManagerKmip/{moId}/UpdateKmsSignedCsrClientCert | Set KMS server signed certificate as KMIP client certificate for the KMS cluster. 
[**crypto_manager_kmip_update_self_signed_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_update_self_signed_client_cert) | **POST** /CryptoManagerKmip/{moId}/UpdateSelfSignedClientCert | Set a self-signed certificate as KMIP client certificate for the KMS cluster. 
[**crypto_manager_kmip_upload_client_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_upload_client_cert) | **POST** /CryptoManagerKmip/{moId}/UploadClientCert | Set a client certificate with private key for the KMIP cluster. 
[**crypto_manager_kmip_upload_kmip_server_cert**](CryptoManagerKmipApi.md#crypto_manager_kmip_upload_kmip_server_cert) | **POST** /CryptoManagerKmip/{moId}/UploadKmipServerCert | Upload a server certficate. 


# **crypto_manager_kmip_add_key**
> crypto_manager_kmip_add_key(mo_id, add_key_request_type)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_key_request_type = vmware_vi.AddKeyRequestType() # AddKeyRequestType | 

    try:
        # Add an existing key. 
        api_instance.crypto_manager_kmip_add_key(mo_id, add_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_add_key: %s\n" % e)
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

# **crypto_manager_kmip_add_keys**
> List[CryptoKeyResult] crypto_manager_kmip_add_keys(mo_id, add_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_keys_request_type = vmware_vi.AddKeysRequestType() # AddKeysRequestType | 

    try:
        # Add multiple existing keys. 
        api_response = api_instance.crypto_manager_kmip_add_keys(mo_id, add_keys_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_add_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_add_keys: %s\n" % e)
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

# **crypto_manager_kmip_generate_client_csr**
> str crypto_manager_kmip_generate_client_csr(mo_id, generate_client_csr_request_type)

Generate a certificate signing request with its private key. 

Generate a certificate signing request with its private key.  This generates a CSR request as well as its private key. The private key will not be returned to caller for security protection. If this method is called again, the CSR and private key generated in the new invocation will overwrite the old ones. After the CSR is signed by KMS into a certificate, it should be updated by calling *CryptoManagerKmip.UpdateKmsSignedCsrClientCert*. The generated CSR can be later retrieved by calling *CryptoManagerKmip.RetrieveClientCsr*.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_client_csr_request_type import GenerateClientCsrRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_client_csr_request_type = vmware_vi.GenerateClientCsrRequestType() # GenerateClientCsrRequestType | 

    try:
        # Generate a certificate signing request with its private key. 
        api_response = api_instance.crypto_manager_kmip_generate_client_csr(mo_id, generate_client_csr_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_generate_client_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_generate_client_csr: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_client_csr_request_type** | [**GenerateClientCsrRequestType**](GenerateClientCsrRequestType.md)|  | 

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
**200** | A newly generated CSR.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_generate_key**
> CryptoKeyResult crypto_manager_kmip_generate_key(mo_id, generate_key_request_type)

Generate new encryption key. 

Generate new encryption key.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_key_result import CryptoKeyResult
from vmware_vi.models.generate_key_request_type import GenerateKeyRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_key_request_type = vmware_vi.GenerateKeyRequestType() # GenerateKeyRequestType | 

    try:
        # Generate new encryption key. 
        api_response = api_instance.crypto_manager_kmip_generate_key(mo_id, generate_key_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_generate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_generate_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_key_request_type** | [**GenerateKeyRequestType**](GenerateKeyRequestType.md)|  | 

### Return type

[**CryptoKeyResult**](CryptoKeyResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the generated key.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_generate_self_signed_client_cert**
> str crypto_manager_kmip_generate_self_signed_client_cert(mo_id, generate_self_signed_client_cert_request_type)

Generate a self-signed client certificate with its private key. 

Generate a self-signed client certificate with its private key.  This generates a self signed certificate as well as its private key. The private key will not be returned to caller for security protection. If this method is called again, the certificate and private key generated in the new invocation will overwrite the old ones. The generated certificate will not replace current working certificate until *CryptoManagerKmip.UpdateSelfSignedClientCert* is called. The generated self signed certificate can be later retrieved by calling *CryptoManagerKmip.RetrieveSelfSignedClientCert*.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_self_signed_client_cert_request_type import GenerateSelfSignedClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_self_signed_client_cert_request_type = vmware_vi.GenerateSelfSignedClientCertRequestType() # GenerateSelfSignedClientCertRequestType | 

    try:
        # Generate a self-signed client certificate with its private key. 
        api_response = api_instance.crypto_manager_kmip_generate_self_signed_client_cert(mo_id, generate_self_signed_client_cert_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_generate_self_signed_client_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_generate_self_signed_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_self_signed_client_cert_request_type** | [**GenerateSelfSignedClientCertRequestType**](GenerateSelfSignedClientCertRequestType.md)|  | 

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
**200** | A new self-signed client certificate.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_get_default_kms_cluster**
> KeyProviderId crypto_manager_kmip_get_default_kms_cluster(mo_id, get_default_kms_cluster_request_type)

Get the default KMS cluster of the specified managed entity. 

Get the default KMS cluster of the specified managed entity.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.get_default_kms_cluster_request_type import GetDefaultKmsClusterRequestType
from vmware_vi.models.key_provider_id import KeyProviderId
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_default_kms_cluster_request_type = vmware_vi.GetDefaultKmsClusterRequestType() # GetDefaultKmsClusterRequestType | 

    try:
        # Get the default KMS cluster of the specified managed entity. 
        api_response = api_instance.crypto_manager_kmip_get_default_kms_cluster(mo_id, get_default_kms_cluster_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_get_default_kms_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_get_default_kms_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_default_kms_cluster_request_type** | [**GetDefaultKmsClusterRequestType**](GetDefaultKmsClusterRequestType.md)|  | 

### Return type

[**KeyProviderId**](KeyProviderId.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The default kms cluster of the entity, if any.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_get_enabled**
> bool crypto_manager_kmip_get_enabled(mo_id)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Indicate if the encryption feature is enabled. 
        api_response = api_instance.crypto_manager_kmip_get_enabled(mo_id)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_get_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_get_enabled: %s\n" % e)
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

# **crypto_manager_kmip_get_kmip_servers**
> List[KmipClusterInfo] crypto_manager_kmip_get_kmip_servers(mo_id)

A list of registered KMIP servers, grouped by clusters. 

A list of registered KMIP servers, grouped by clusters.  ***Since:*** vSphere API 6.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.kmip_cluster_info import KmipClusterInfo
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of registered KMIP servers, grouped by clusters. 
        api_response = api_instance.crypto_manager_kmip_get_kmip_servers(mo_id)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_get_kmip_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_get_kmip_servers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[KmipClusterInfo]**](KmipClusterInfo.md)

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

# **crypto_manager_kmip_is_kms_cluster_active**
> bool crypto_manager_kmip_is_kms_cluster_active(mo_id, is_kms_cluster_active_request_type)

Check whether an active KMS exists in cluster. 

Check whether an active KMS exists in cluster.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.is_kms_cluster_active_request_type import IsKmsClusterActiveRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    is_kms_cluster_active_request_type = vmware_vi.IsKmsClusterActiveRequestType() # IsKmsClusterActiveRequestType | 

    try:
        # Check whether an active KMS exists in cluster. 
        api_response = api_instance.crypto_manager_kmip_is_kms_cluster_active(mo_id, is_kms_cluster_active_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_is_kms_cluster_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_is_kms_cluster_active: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **is_kms_cluster_active_request_type** | [**IsKmsClusterActiveRequestType**](IsKmsClusterActiveRequestType.md)|  | 

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
**200** | true if active KMS exists in cluster, false otherwise.  |  -  |
**500** | ***InvalidArgument***: in case the cluster is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_list_keys**
> List[CryptoKeyId] crypto_manager_kmip_list_keys(mo_id, list_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_keys_request_type = vmware_vi.ListKeysRequestType() # ListKeysRequestType | 

    try:
        # List keys. 
        api_response = api_instance.crypto_manager_kmip_list_keys(mo_id, list_keys_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_list_keys: %s\n" % e)
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

# **crypto_manager_kmip_list_kmip_servers**
> List[KmipClusterInfo] crypto_manager_kmip_list_kmip_servers(mo_id, list_kmip_servers_request_type)

List the registered KMIP servers. 

List the registered KMIP servers.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.kmip_cluster_info import KmipClusterInfo
from vmware_vi.models.list_kmip_servers_request_type import ListKmipServersRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_kmip_servers_request_type = vmware_vi.ListKmipServersRequestType() # ListKmipServersRequestType | 

    try:
        # List the registered KMIP servers. 
        api_response = api_instance.crypto_manager_kmip_list_kmip_servers(mo_id, list_kmip_servers_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_list_kmip_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_list_kmip_servers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_kmip_servers_request_type** | [**ListKmipServersRequestType**](ListKmipServersRequestType.md)|  | 

### Return type

[**List[KmipClusterInfo]**](KmipClusterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of known KMIP servers grouped in clusters.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_list_kms_clusters**
> List[KmipClusterInfo] crypto_manager_kmip_list_kms_clusters(mo_id, list_kms_clusters_request_type)

List the KMS clusters information. 

List the KMS clusters information.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.kmip_cluster_info import KmipClusterInfo
from vmware_vi.models.list_kms_clusters_request_type import ListKmsClustersRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_kms_clusters_request_type = vmware_vi.ListKmsClustersRequestType() # ListKmsClustersRequestType | 

    try:
        # List the KMS clusters information. 
        api_response = api_instance.crypto_manager_kmip_list_kms_clusters(mo_id, list_kms_clusters_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_list_kms_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_list_kms_clusters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_kms_clusters_request_type** | [**ListKmsClustersRequestType**](ListKmsClustersRequestType.md)|  | 

### Return type

[**List[KmipClusterInfo]**](KmipClusterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Key Providers.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_mark_default**
> crypto_manager_kmip_mark_default(mo_id, mark_default_request_type)

Set the default KMIP cluster. 

Set the default KMIP cluster.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mark_default_request_type import MarkDefaultRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_default_request_type = vmware_vi.MarkDefaultRequestType() # MarkDefaultRequestType | 

    try:
        # Set the default KMIP cluster. 
        api_instance.crypto_manager_kmip_mark_default(mo_id, mark_default_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_mark_default: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_default_request_type** | [**MarkDefaultRequestType**](MarkDefaultRequestType.md)|  | 

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

# **crypto_manager_kmip_query_crypto_key_status**
> List[CryptoManagerKmipCryptoKeyStatus] crypto_manager_kmip_query_crypto_key_status(mo_id, query_crypto_key_status_request_type)

Check CryptoKey status, such as if VC can access the key, if the key is used by some VMs or as host key. 

Check CryptoKey status, such as if VC can access the key, if the key is used by some VMs or as host key.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_manager_kmip_crypto_key_status import CryptoManagerKmipCryptoKeyStatus
from vmware_vi.models.query_crypto_key_status_request_type import QueryCryptoKeyStatusRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_crypto_key_status_request_type = vmware_vi.QueryCryptoKeyStatusRequestType() # QueryCryptoKeyStatusRequestType | 

    try:
        # Check CryptoKey status, such as if VC can access the key, if the key is used by some VMs or as host key. 
        api_response = api_instance.crypto_manager_kmip_query_crypto_key_status(mo_id, query_crypto_key_status_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_query_crypto_key_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_query_crypto_key_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_crypto_key_status_request_type** | [**QueryCryptoKeyStatusRequestType**](QueryCryptoKeyStatusRequestType.md)|  | 

### Return type

[**List[CryptoManagerKmipCryptoKeyStatus]**](CryptoManagerKmipCryptoKeyStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The structure combined with key status. If bit in parameter is not set when invoke, the returned data in related CryptoKeyStatus will be unknown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_register_kmip_server**
> crypto_manager_kmip_register_kmip_server(mo_id, register_kmip_server_request_type)

Register a KMIP server. 

Register a KMIP server.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.register_kmip_server_request_type import RegisterKmipServerRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_kmip_server_request_type = vmware_vi.RegisterKmipServerRequestType() # RegisterKmipServerRequestType | 

    try:
        # Register a KMIP server. 
        api_instance.crypto_manager_kmip_register_kmip_server(mo_id, register_kmip_server_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_register_kmip_server: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_kmip_server_request_type** | [**RegisterKmipServerRequestType**](RegisterKmipServerRequestType.md)|  | 

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

# **crypto_manager_kmip_register_kms_cluster**
> crypto_manager_kmip_register_kms_cluster(mo_id, register_kms_cluster_request_type)

Register the specified KMS cluster to the CryptoManager. 

Register the specified KMS cluster to the CryptoManager.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.register_kms_cluster_request_type import RegisterKmsClusterRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_kms_cluster_request_type = vmware_vi.RegisterKmsClusterRequestType() # RegisterKmsClusterRequestType | 

    try:
        # Register the specified KMS cluster to the CryptoManager. 
        api_instance.crypto_manager_kmip_register_kms_cluster(mo_id, register_kms_cluster_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_register_kms_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_kms_cluster_request_type** | [**RegisterKmsClusterRequestType**](RegisterKmsClusterRequestType.md)|  | 

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

# **crypto_manager_kmip_remove_key**
> crypto_manager_kmip_remove_key(mo_id, remove_key_request_type)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_key_request_type = vmware_vi.RemoveKeyRequestType() # RemoveKeyRequestType | 

    try:
        # Remove a key (only the UUID is needed to remove). 
        api_instance.crypto_manager_kmip_remove_key(mo_id, remove_key_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_remove_key: %s\n" % e)
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

# **crypto_manager_kmip_remove_keys**
> List[CryptoKeyResult] crypto_manager_kmip_remove_keys(mo_id, remove_keys_request_type)

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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_keys_request_type = vmware_vi.RemoveKeysRequestType() # RemoveKeysRequestType | 

    try:
        # Remove multiple keys (only the UUID is needed to remove). 
        api_response = api_instance.crypto_manager_kmip_remove_keys(mo_id, remove_keys_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_remove_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_remove_keys: %s\n" % e)
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

# **crypto_manager_kmip_remove_kmip_server**
> crypto_manager_kmip_remove_kmip_server(mo_id, remove_kmip_server_request_type)

Remove a KMIP server, even if in use. 

Remove a KMIP server, even if in use.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_kmip_server_request_type import RemoveKmipServerRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_kmip_server_request_type = vmware_vi.RemoveKmipServerRequestType() # RemoveKmipServerRequestType | 

    try:
        # Remove a KMIP server, even if in use. 
        api_instance.crypto_manager_kmip_remove_kmip_server(mo_id, remove_kmip_server_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_remove_kmip_server: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_kmip_server_request_type** | [**RemoveKmipServerRequestType**](RemoveKmipServerRequestType.md)|  | 

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

# **crypto_manager_kmip_retrieve_client_cert**
> str crypto_manager_kmip_retrieve_client_cert(mo_id, retrieve_client_cert_request_type)

Get the client certificate of the KMIP cluster. 

Get the client certificate of the KMIP cluster.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_client_cert_request_type import RetrieveClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_client_cert_request_type = vmware_vi.RetrieveClientCertRequestType() # RetrieveClientCertRequestType | 

    try:
        # Get the client certificate of the KMIP cluster. 
        api_response = api_instance.crypto_manager_kmip_retrieve_client_cert(mo_id, retrieve_client_cert_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_retrieve_client_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_retrieve_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_client_cert_request_type** | [**RetrieveClientCertRequestType**](RetrieveClientCertRequestType.md)|  | 

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
**200** | The client certificate.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_retrieve_client_csr**
> str crypto_manager_kmip_retrieve_client_csr(mo_id, retrieve_client_csr_request_type)

Get the generated client certificate signing request. 

Get the generated client certificate signing request.  If *CryptoManagerKmip.GenerateClientCsr* is called previously, this will return the generated certificate signing request; otherwise return empty string.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_client_csr_request_type import RetrieveClientCsrRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_client_csr_request_type = vmware_vi.RetrieveClientCsrRequestType() # RetrieveClientCsrRequestType | 

    try:
        # Get the generated client certificate signing request. 
        api_response = api_instance.crypto_manager_kmip_retrieve_client_csr(mo_id, retrieve_client_csr_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_retrieve_client_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_retrieve_client_csr: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_client_csr_request_type** | [**RetrieveClientCsrRequestType**](RetrieveClientCsrRequestType.md)|  | 

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
**200** | The CSR generated previously, if any.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_retrieve_kmip_server_cert**
> CryptoManagerKmipServerCertInfo crypto_manager_kmip_retrieve_kmip_server_cert(mo_id, retrieve_kmip_server_cert_request_type)

Get the server certficate. 

Get the server certficate.  In the case of error, an empty certificate string is returned.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_manager_kmip_server_cert_info import CryptoManagerKmipServerCertInfo
from vmware_vi.models.retrieve_kmip_server_cert_request_type import RetrieveKmipServerCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_kmip_server_cert_request_type = vmware_vi.RetrieveKmipServerCertRequestType() # RetrieveKmipServerCertRequestType | 

    try:
        # Get the server certficate. 
        api_response = api_instance.crypto_manager_kmip_retrieve_kmip_server_cert(mo_id, retrieve_kmip_server_cert_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_retrieve_kmip_server_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_retrieve_kmip_server_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_kmip_server_cert_request_type** | [**RetrieveKmipServerCertRequestType**](RetrieveKmipServerCertRequestType.md)|  | 

### Return type

[**CryptoManagerKmipServerCertInfo**](CryptoManagerKmipServerCertInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the server certificate.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_retrieve_kmip_servers_status_task**
> ManagedObjectReference crypto_manager_kmip_retrieve_kmip_servers_status_task(mo_id, retrieve_kmip_servers_status_request_type)

Get the status of the KMIP servers. 

Get the status of the KMIP servers.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.retrieve_kmip_servers_status_request_type import RetrieveKmipServersStatusRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_kmip_servers_status_request_type = vmware_vi.RetrieveKmipServersStatusRequestType() # RetrieveKmipServersStatusRequestType | 

    try:
        # Get the status of the KMIP servers. 
        api_response = api_instance.crypto_manager_kmip_retrieve_kmip_servers_status_task(mo_id, retrieve_kmip_servers_status_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_retrieve_kmip_servers_status_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_retrieve_kmip_servers_status_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_kmip_servers_status_request_type** | [**RetrieveKmipServersStatusRequestType**](RetrieveKmipServersStatusRequestType.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_retrieve_self_signed_client_cert**
> str crypto_manager_kmip_retrieve_self_signed_client_cert(mo_id, retrieve_self_signed_client_cert_request_type)

Get the generated self signed client certificate. 

Get the generated self signed client certificate.  If *CryptoManagerKmip.GenerateSelfSignedClientCert* is called previously, this will return the generated certificate; otherwise return empty string.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_self_signed_client_cert_request_type import RetrieveSelfSignedClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_self_signed_client_cert_request_type = vmware_vi.RetrieveSelfSignedClientCertRequestType() # RetrieveSelfSignedClientCertRequestType | 

    try:
        # Get the generated self signed client certificate. 
        api_response = api_instance.crypto_manager_kmip_retrieve_self_signed_client_cert(mo_id, retrieve_self_signed_client_cert_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_retrieve_self_signed_client_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_retrieve_self_signed_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_self_signed_client_cert_request_type** | [**RetrieveSelfSignedClientCertRequestType**](RetrieveSelfSignedClientCertRequestType.md)|  | 

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
**200** | The self signed certificate generated previously, if any.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_set_default_kms_cluster**
> crypto_manager_kmip_set_default_kms_cluster(mo_id, set_default_kms_cluster_request_type)

Set the default KMS cluster for the specified managed entity. 

Set the default KMS cluster for the specified managed entity.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_default_kms_cluster_request_type import SetDefaultKmsClusterRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_default_kms_cluster_request_type = vmware_vi.SetDefaultKmsClusterRequestType() # SetDefaultKmsClusterRequestType | 

    try:
        # Set the default KMS cluster for the specified managed entity. 
        api_instance.crypto_manager_kmip_set_default_kms_cluster(mo_id, set_default_kms_cluster_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_set_default_kms_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_default_kms_cluster_request_type** | [**SetDefaultKmsClusterRequestType**](SetDefaultKmsClusterRequestType.md)|  | 

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

# **crypto_manager_kmip_set_key_custom_attributes**
> CryptoKeyResult crypto_manager_kmip_set_key_custom_attributes(mo_id, set_key_custom_attributes_request_type)

Set crypto key's custom attributes. 

Set crypto key's custom attributes.  ***Required privileges:*** Cryptographer.ManageKeys 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.crypto_key_result import CryptoKeyResult
from vmware_vi.models.set_key_custom_attributes_request_type import SetKeyCustomAttributesRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_key_custom_attributes_request_type = vmware_vi.SetKeyCustomAttributesRequestType() # SetKeyCustomAttributesRequestType | 

    try:
        # Set crypto key's custom attributes. 
        api_response = api_instance.crypto_manager_kmip_set_key_custom_attributes(mo_id, set_key_custom_attributes_request_type)
        print("The response of CryptoManagerKmipApi->crypto_manager_kmip_set_key_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_set_key_custom_attributes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_key_custom_attributes_request_type** | [**SetKeyCustomAttributesRequestType**](SetKeyCustomAttributesRequestType.md)|  | 

### Return type

[**CryptoKeyResult**](CryptoKeyResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The structure combined with status and fail reason.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_manager_kmip_unregister_kms_cluster**
> crypto_manager_kmip_unregister_kms_cluster(mo_id, unregister_kms_cluster_request_type)

Unregister the specified KMS cluster from the CryptoManager. 

Unregister the specified KMS cluster from the CryptoManager.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unregister_kms_cluster_request_type import UnregisterKmsClusterRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unregister_kms_cluster_request_type = vmware_vi.UnregisterKmsClusterRequestType() # UnregisterKmsClusterRequestType | 

    try:
        # Unregister the specified KMS cluster from the CryptoManager. 
        api_instance.crypto_manager_kmip_unregister_kms_cluster(mo_id, unregister_kms_cluster_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_unregister_kms_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unregister_kms_cluster_request_type** | [**UnregisterKmsClusterRequestType**](UnregisterKmsClusterRequestType.md)|  | 

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

# **crypto_manager_kmip_update_kmip_server**
> crypto_manager_kmip_update_kmip_server(mo_id, update_kmip_server_request_type)

Update a KMIP server. 

Update a KMIP server.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_kmip_server_request_type import UpdateKmipServerRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_kmip_server_request_type = vmware_vi.UpdateKmipServerRequestType() # UpdateKmipServerRequestType | 

    try:
        # Update a KMIP server. 
        api_instance.crypto_manager_kmip_update_kmip_server(mo_id, update_kmip_server_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_update_kmip_server: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_kmip_server_request_type** | [**UpdateKmipServerRequestType**](UpdateKmipServerRequestType.md)|  | 

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

# **crypto_manager_kmip_update_kms_signed_csr_client_cert**
> crypto_manager_kmip_update_kms_signed_csr_client_cert(mo_id, update_kms_signed_csr_client_cert_request_type)

Set KMS server signed certificate as KMIP client certificate for the KMS cluster. 

Set KMS server signed certificate as KMIP client certificate for the KMS cluster.  This method should be called to update the certificate signed by KMS server from a CSR that is generated by calling *CryptoManagerKmip.GenerateClientCsr*. If *CryptoManagerKmip.GenerateClientCsr* is called more than once, the CSR that is generated last time should be used; otherwise the certificate will be rejected because the private key from last time won't match the public key in the certificate.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_kms_signed_csr_client_cert_request_type import UpdateKmsSignedCsrClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_kms_signed_csr_client_cert_request_type = vmware_vi.UpdateKmsSignedCsrClientCertRequestType() # UpdateKmsSignedCsrClientCertRequestType | 

    try:
        # Set KMS server signed certificate as KMIP client certificate for the KMS cluster. 
        api_instance.crypto_manager_kmip_update_kms_signed_csr_client_cert(mo_id, update_kms_signed_csr_client_cert_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_update_kms_signed_csr_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_kms_signed_csr_client_cert_request_type** | [**UpdateKmsSignedCsrClientCertRequestType**](UpdateKmsSignedCsrClientCertRequestType.md)|  | 

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

# **crypto_manager_kmip_update_self_signed_client_cert**
> crypto_manager_kmip_update_self_signed_client_cert(mo_id, update_self_signed_client_cert_request_type)

Set a self-signed certificate as KMIP client certificate for the KMS cluster. 

Set a self-signed certificate as KMIP client certificate for the KMS cluster.  This method should be called to update the certificate which is generated by calling *CryptoManagerKmip.GenerateSelfSignedClientCert*. If *CryptoManagerKmip.GenerateSelfSignedClientCert* is called more than once, the self signed certificate that is generated last time should be used; otherwise the certificate will be rejected because the private key from last time won't match the public key in the certificate.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_self_signed_client_cert_request_type import UpdateSelfSignedClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_self_signed_client_cert_request_type = vmware_vi.UpdateSelfSignedClientCertRequestType() # UpdateSelfSignedClientCertRequestType | 

    try:
        # Set a self-signed certificate as KMIP client certificate for the KMS cluster. 
        api_instance.crypto_manager_kmip_update_self_signed_client_cert(mo_id, update_self_signed_client_cert_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_update_self_signed_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_self_signed_client_cert_request_type** | [**UpdateSelfSignedClientCertRequestType**](UpdateSelfSignedClientCertRequestType.md)|  | 

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

# **crypto_manager_kmip_upload_client_cert**
> crypto_manager_kmip_upload_client_cert(mo_id, upload_client_cert_request_type)

Set a client certificate with private key for the KMIP cluster. 

Set a client certificate with private key for the KMIP cluster.  The certificate and private key can be assigned by a KMS server and the certificate might be already trusted by the KMS server.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.upload_client_cert_request_type import UploadClientCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upload_client_cert_request_type = vmware_vi.UploadClientCertRequestType() # UploadClientCertRequestType | 

    try:
        # Set a client certificate with private key for the KMIP cluster. 
        api_instance.crypto_manager_kmip_upload_client_cert(mo_id, upload_client_cert_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_upload_client_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upload_client_cert_request_type** | [**UploadClientCertRequestType**](UploadClientCertRequestType.md)|  | 

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

# **crypto_manager_kmip_upload_kmip_server_cert**
> crypto_manager_kmip_upload_kmip_server_cert(mo_id, upload_kmip_server_cert_request_type)

Upload a server certficate. 

Upload a server certficate.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Cryptographer.ManageKeyServers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.upload_kmip_server_cert_request_type import UploadKmipServerCertRequestType
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
    api_instance = vmware_vi.CryptoManagerKmipApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upload_kmip_server_cert_request_type = vmware_vi.UploadKmipServerCertRequestType() # UploadKmipServerCertRequestType | 

    try:
        # Upload a server certficate. 
        api_instance.crypto_manager_kmip_upload_kmip_server_cert(mo_id, upload_kmip_server_cert_request_type)
    except Exception as e:
        print("Exception when calling CryptoManagerKmipApi->crypto_manager_kmip_upload_kmip_server_cert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upload_kmip_server_cert_request_type** | [**UploadKmipServerCertRequestType**](UploadKmipServerCertRequestType.md)|  | 

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

