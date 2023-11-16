# vmware_vi.HostCertificateManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_certificate_manager_generate_certificate_signing_request**](HostCertificateManagerApi.md#host_certificate_manager_generate_certificate_signing_request) | **POST** /HostCertificateManager/{moId}/GenerateCertificateSigningRequest | Requests the server to generate a certificate-signing request (CSR) for itself. 
[**host_certificate_manager_generate_certificate_signing_request_by_dn**](HostCertificateManagerApi.md#host_certificate_manager_generate_certificate_signing_request_by_dn) | **POST** /HostCertificateManager/{moId}/GenerateCertificateSigningRequestByDn | Requests the server to generate a certificate-signing request (CSR) for itself. 
[**host_certificate_manager_get_certificate_info**](HostCertificateManagerApi.md#host_certificate_manager_get_certificate_info) | **GET** /HostCertificateManager/{moId}/certificateInfo | the CertificateInfo of the Host Certificate. 
[**host_certificate_manager_install_server_certificate**](HostCertificateManagerApi.md#host_certificate_manager_install_server_certificate) | **POST** /HostCertificateManager/{moId}/InstallServerCertificate | Installs a given SSL certificate on the server. 
[**host_certificate_manager_list_ca_certificate_revocation_lists**](HostCertificateManagerApi.md#host_certificate_manager_list_ca_certificate_revocation_lists) | **POST** /HostCertificateManager/{moId}/ListCACertificateRevocationLists | Fetches the SSL CRLs of Certificate Authorities that are trusted. 
[**host_certificate_manager_list_ca_certificates**](HostCertificateManagerApi.md#host_certificate_manager_list_ca_certificates) | **POST** /HostCertificateManager/{moId}/ListCACertificates | Fetches the SSL certificates of Certificate Authorities that are trusted. 
[**host_certificate_manager_replace_ca_certificates_and_crls**](HostCertificateManagerApi.md#host_certificate_manager_replace_ca_certificates_and_crls) | **POST** /HostCertificateManager/{moId}/ReplaceCACertificatesAndCRLs | Replaces the trusted Certificate Authority (CA) certificates and Certification Revocation List (CRL) used by the server with the provided values. 
[**host_certificate_manager_retrieve_certificate_info_list**](HostCertificateManagerApi.md#host_certificate_manager_retrieve_certificate_info_list) | **POST** /HostCertificateManager/{moId}/RetrieveCertificateInfoList | the CertificateInfos of all known Certificates on the host 


# **host_certificate_manager_generate_certificate_signing_request**
> str host_certificate_manager_generate_certificate_signing_request(mo_id, generate_certificate_signing_request_request_type)

Requests the server to generate a certificate-signing request (CSR) for itself. 

Requests the server to generate a certificate-signing request (CSR) for itself.  The CSR is then typically provided to a Certificate Authority to sign and issue the SSL certificate for the server. Use *HostCertificateManager.InstallServerCertificate* to install this certificate.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_certificate_signing_request_request_type import GenerateCertificateSigningRequestRequestType
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_certificate_signing_request_request_type = vmware_vi.GenerateCertificateSigningRequestRequestType() # GenerateCertificateSigningRequestRequestType | 

    try:
        # Requests the server to generate a certificate-signing request (CSR) for itself. 
        api_response = api_instance.host_certificate_manager_generate_certificate_signing_request(mo_id, generate_certificate_signing_request_request_type)
        print("The response of HostCertificateManagerApi->host_certificate_manager_generate_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_generate_certificate_signing_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_certificate_signing_request_request_type** | [**GenerateCertificateSigningRequestRequestType**](GenerateCertificateSigningRequestRequestType.md)|  | 

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
**200** | CSR in PEM format  |  -  |
**500** | ***HostConfigFault***: if there&#39;s a problem generating the CSR.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_generate_certificate_signing_request_by_dn**
> str host_certificate_manager_generate_certificate_signing_request_by_dn(mo_id, generate_certificate_signing_request_by_dn_request_type)

Requests the server to generate a certificate-signing request (CSR) for itself. 

Requests the server to generate a certificate-signing request (CSR) for itself.  Alternative version similar to *HostCertificateManager.GenerateCertificateSigningRequest* but takes a Distinguished Name (DN) as a parameter.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_certificate_signing_request_by_dn_request_type import GenerateCertificateSigningRequestByDnRequestType
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_certificate_signing_request_by_dn_request_type = vmware_vi.GenerateCertificateSigningRequestByDnRequestType() # GenerateCertificateSigningRequestByDnRequestType | 

    try:
        # Requests the server to generate a certificate-signing request (CSR) for itself. 
        api_response = api_instance.host_certificate_manager_generate_certificate_signing_request_by_dn(mo_id, generate_certificate_signing_request_by_dn_request_type)
        print("The response of HostCertificateManagerApi->host_certificate_manager_generate_certificate_signing_request_by_dn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_generate_certificate_signing_request_by_dn: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_certificate_signing_request_by_dn_request_type** | [**GenerateCertificateSigningRequestByDnRequestType**](GenerateCertificateSigningRequestByDnRequestType.md)|  | 

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
**200** | CSR in PEM format  |  -  |
**500** | ***HostConfigFault***: if there&#39;s a problem generating the CSR.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_get_certificate_info**
> HostCertificateManagerCertificateInfo host_certificate_manager_get_certificate_info(mo_id)

the CertificateInfo of the Host Certificate. 

the CertificateInfo of the Host Certificate.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_certificate_manager_certificate_info import HostCertificateManagerCertificateInfo
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # the CertificateInfo of the Host Certificate. 
        api_response = api_instance.host_certificate_manager_get_certificate_info(mo_id)
        print("The response of HostCertificateManagerApi->host_certificate_manager_get_certificate_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_get_certificate_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostCertificateManagerCertificateInfo**](HostCertificateManagerCertificateInfo.md)

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

# **host_certificate_manager_install_server_certificate**
> host_certificate_manager_install_server_certificate(mo_id, install_server_certificate_request_type)

Installs a given SSL certificate on the server. 

Installs a given SSL certificate on the server.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.install_server_certificate_request_type import InstallServerCertificateRequestType
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    install_server_certificate_request_type = vmware_vi.InstallServerCertificateRequestType() # InstallServerCertificateRequestType | 

    try:
        # Installs a given SSL certificate on the server. 
        api_instance.host_certificate_manager_install_server_certificate(mo_id, install_server_certificate_request_type)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_install_server_certificate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **install_server_certificate_request_type** | [**InstallServerCertificateRequestType**](InstallServerCertificateRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if there&#39;s a problem with the input certificate.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_list_ca_certificate_revocation_lists**
> List[str] host_certificate_manager_list_ca_certificate_revocation_lists(mo_id)

Fetches the SSL CRLs of Certificate Authorities that are trusted. 

Fetches the SSL CRLs of Certificate Authorities that are trusted.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Fetches the SSL CRLs of Certificate Authorities that are trusted. 
        api_response = api_instance.host_certificate_manager_list_ca_certificate_revocation_lists(mo_id)
        print("The response of HostCertificateManagerApi->host_certificate_manager_list_ca_certificate_revocation_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_list_ca_certificate_revocation_lists: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSL CRLs of trusted CAs in PEM format  |  -  |
**500** | ***HostConfigFault***: if there&#39;s a problem with the certificate store.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_list_ca_certificates**
> List[str] host_certificate_manager_list_ca_certificates(mo_id)

Fetches the SSL certificates of Certificate Authorities that are trusted. 

Fetches the SSL certificates of Certificate Authorities that are trusted.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Fetches the SSL certificates of Certificate Authorities that are trusted. 
        api_response = api_instance.host_certificate_manager_list_ca_certificates(mo_id)
        print("The response of HostCertificateManagerApi->host_certificate_manager_list_ca_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_list_ca_certificates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSL certificates of trusted CAs in PEM format  |  -  |
**500** | ***HostConfigFault***: if there&#39;s a problem with the certificate store.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_replace_ca_certificates_and_crls**
> host_certificate_manager_replace_ca_certificates_and_crls(mo_id, replace_ca_certificates_and_crls_request_type)

Replaces the trusted Certificate Authority (CA) certificates and Certification Revocation List (CRL) used by the server with the provided values. 

Replaces the trusted Certificate Authority (CA) certificates and Certification Revocation List (CRL) used by the server with the provided values.  These determine whether the server can verify the identity of an external entity.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.replace_ca_certificates_and_crls_request_type import ReplaceCACertificatesAndCRLsRequestType
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    replace_ca_certificates_and_crls_request_type = vmware_vi.ReplaceCACertificatesAndCRLsRequestType() # ReplaceCACertificatesAndCRLsRequestType | 

    try:
        # Replaces the trusted Certificate Authority (CA) certificates and Certification Revocation List (CRL) used by the server with the provided values. 
        api_instance.host_certificate_manager_replace_ca_certificates_and_crls(mo_id, replace_ca_certificates_and_crls_request_type)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_replace_ca_certificates_and_crls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **replace_ca_certificates_and_crls_request_type** | [**ReplaceCACertificatesAndCRLsRequestType**](ReplaceCACertificatesAndCRLsRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if there&#39;s a problem with the input certificates or CRLs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_certificate_manager_retrieve_certificate_info_list**
> List[HostCertificateManagerCertificateInfo] host_certificate_manager_retrieve_certificate_info_list(mo_id)

the CertificateInfos of all known Certificates on the host 

the CertificateInfos of all known Certificates on the host  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_certificate_manager_certificate_info import HostCertificateManagerCertificateInfo
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
    api_instance = vmware_vi.HostCertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # the CertificateInfos of all known Certificates on the host 
        api_response = api_instance.host_certificate_manager_retrieve_certificate_info_list(mo_id)
        print("The response of HostCertificateManagerApi->host_certificate_manager_retrieve_certificate_info_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCertificateManagerApi->host_certificate_manager_retrieve_certificate_info_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostCertificateManagerCertificateInfo]**](HostCertificateManagerCertificateInfo.md)

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

