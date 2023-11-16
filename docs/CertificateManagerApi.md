# vmware_vi.CertificateManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task**](CertificateManagerApi.md#certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task) | **POST** /CertificateManager/{moId}/CertMgrRefreshCACertificatesAndCRLs_Task | Re-fetches certificates of trusted CAs and the Certificate Revocation Lists (CRL) from the appropriate authoritative source and pushes them to the hosts. 
[**certificate_manager_cert_mgr_refresh_certificates_task**](CertificateManagerApi.md#certificate_manager_cert_mgr_refresh_certificates_task) | **POST** /CertificateManager/{moId}/CertMgrRefreshCertificates_Task | Gets CSRs from the hosts and then gets these certificates signed by the VMware Certificate Service and pushes them down to the hosts. 
[**certificate_manager_cert_mgr_revoke_certificates_task**](CertificateManagerApi.md#certificate_manager_cert_mgr_revoke_certificates_task) | **POST** /CertificateManager/{moId}/CertMgrRevokeCertificates_Task | Revokes the certificates of some hosts. 


# **certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task**
> ManagedObjectReference certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task(mo_id, cert_mgr_refresh_ca_certificates_and_crls_request_type)

Re-fetches certificates of trusted CAs and the Certificate Revocation Lists (CRL) from the appropriate authoritative source and pushes them to the hosts. 

Re-fetches certificates of trusted CAs and the Certificate Revocation Lists (CRL) from the appropriate authoritative source and pushes them to the hosts.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cert_mgr_refresh_ca_certificates_and_crls_request_type import CertMgrRefreshCACertificatesAndCRLsRequestType
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
    api_instance = vmware_vi.CertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cert_mgr_refresh_ca_certificates_and_crls_request_type = vmware_vi.CertMgrRefreshCACertificatesAndCRLsRequestType() # CertMgrRefreshCACertificatesAndCRLsRequestType | 

    try:
        # Re-fetches certificates of trusted CAs and the Certificate Revocation Lists (CRL) from the appropriate authoritative source and pushes them to the hosts. 
        api_response = api_instance.certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task(mo_id, cert_mgr_refresh_ca_certificates_and_crls_request_type)
        print("The response of CertificateManagerApi->certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagerApi->certificate_manager_cert_mgr_refresh_ca_certificates_and_crls_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cert_mgr_refresh_ca_certificates_and_crls_request_type** | [**CertMgrRefreshCACertificatesAndCRLsRequestType**](CertMgrRefreshCACertificatesAndCRLsRequestType.md)|  | 

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

# **certificate_manager_cert_mgr_refresh_certificates_task**
> ManagedObjectReference certificate_manager_cert_mgr_refresh_certificates_task(mo_id, cert_mgr_refresh_certificates_request_type)

Gets CSRs from the hosts and then gets these certificates signed by the VMware Certificate Service and pushes them down to the hosts. 

Gets CSRs from the hosts and then gets these certificates signed by the VMware Certificate Service and pushes them down to the hosts.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cert_mgr_refresh_certificates_request_type import CertMgrRefreshCertificatesRequestType
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
    api_instance = vmware_vi.CertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cert_mgr_refresh_certificates_request_type = vmware_vi.CertMgrRefreshCertificatesRequestType() # CertMgrRefreshCertificatesRequestType | 

    try:
        # Gets CSRs from the hosts and then gets these certificates signed by the VMware Certificate Service and pushes them down to the hosts. 
        api_response = api_instance.certificate_manager_cert_mgr_refresh_certificates_task(mo_id, cert_mgr_refresh_certificates_request_type)
        print("The response of CertificateManagerApi->certificate_manager_cert_mgr_refresh_certificates_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagerApi->certificate_manager_cert_mgr_refresh_certificates_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cert_mgr_refresh_certificates_request_type** | [**CertMgrRefreshCertificatesRequestType**](CertMgrRefreshCertificatesRequestType.md)|  | 

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

# **certificate_manager_cert_mgr_revoke_certificates_task**
> ManagedObjectReference certificate_manager_cert_mgr_revoke_certificates_task(mo_id, cert_mgr_revoke_certificates_request_type)

Revokes the certificates of some hosts. 

Revokes the certificates of some hosts.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Certificate.Manage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cert_mgr_revoke_certificates_request_type import CertMgrRevokeCertificatesRequestType
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
    api_instance = vmware_vi.CertificateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cert_mgr_revoke_certificates_request_type = vmware_vi.CertMgrRevokeCertificatesRequestType() # CertMgrRevokeCertificatesRequestType | 

    try:
        # Revokes the certificates of some hosts. 
        api_response = api_instance.certificate_manager_cert_mgr_revoke_certificates_task(mo_id, cert_mgr_revoke_certificates_request_type)
        print("The response of CertificateManagerApi->certificate_manager_cert_mgr_revoke_certificates_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagerApi->certificate_manager_cert_mgr_revoke_certificates_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cert_mgr_revoke_certificates_request_type** | [**CertMgrRevokeCertificatesRequestType**](CertMgrRevokeCertificatesRequestType.md)|  | 

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

