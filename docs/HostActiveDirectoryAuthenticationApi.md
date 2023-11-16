# vmware_vi.HostActiveDirectoryAuthenticationApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_active_directory_authentication_disable_smart_card_authentication**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_disable_smart_card_authentication) | **POST** /HostActiveDirectoryAuthentication/{moId}/DisableSmartCardAuthentication | Disables console authentication using a local smart card and reader. 
[**host_active_directory_authentication_enable_smart_card_authentication**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_enable_smart_card_authentication) | **POST** /HostActiveDirectoryAuthentication/{moId}/EnableSmartCardAuthentication | Enables console authentication using a local smart card and reader. 
[**host_active_directory_authentication_get_info**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_get_info) | **GET** /HostActiveDirectoryAuthentication/{moId}/info | Information about the authentication store. 
[**host_active_directory_authentication_import_certificate_for_cam_task**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_import_certificate_for_cam_task) | **POST** /HostActiveDirectoryAuthentication/{moId}/ImportCertificateForCAM_Task | Import the CAM server&#39;s certificate to the local store of vmwauth. 
[**host_active_directory_authentication_install_smart_card_trust_anchor**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_install_smart_card_trust_anchor) | **POST** /HostActiveDirectoryAuthentication/{moId}/InstallSmartCardTrustAnchor | Install a trust anchor certificate for smart card authentication. 
[**host_active_directory_authentication_join_domain_task**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_join_domain_task) | **POST** /HostActiveDirectoryAuthentication/{moId}/JoinDomain_Task | Adds the host to an Active Directory domain. 
[**host_active_directory_authentication_join_domain_with_cam_task**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_join_domain_with_cam_task) | **POST** /HostActiveDirectoryAuthentication/{moId}/JoinDomainWithCAM_Task | Adds the host to an Active Directory domain through CAM service. 
[**host_active_directory_authentication_leave_current_domain_task**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_leave_current_domain_task) | **POST** /HostActiveDirectoryAuthentication/{moId}/LeaveCurrentDomain_Task | Removes the host from the Active Directory domain to which it belongs. 
[**host_active_directory_authentication_list_smart_card_trust_anchors**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_list_smart_card_trust_anchors) | **POST** /HostActiveDirectoryAuthentication/{moId}/ListSmartCardTrustAnchors | Lists installed trust anchor certificates for smart card authentication. 
[**host_active_directory_authentication_remove_smart_card_trust_anchor**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_remove_smart_card_trust_anchor) | **POST** /HostActiveDirectoryAuthentication/{moId}/RemoveSmartCardTrustAnchor | Remove a smart card trust anchor certificate from the system. 
[**host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint) | **POST** /HostActiveDirectoryAuthentication/{moId}/RemoveSmartCardTrustAnchorByFingerprint | Remove a smart card trust anchor certificate from the system by fingerprint. 
[**host_active_directory_authentication_replace_smart_card_trust_anchors**](HostActiveDirectoryAuthenticationApi.md#host_active_directory_authentication_replace_smart_card_trust_anchors) | **POST** /HostActiveDirectoryAuthentication/{moId}/ReplaceSmartCardTrustAnchors | Replace the trust anchor certificates for smart card authentication. 


# **host_active_directory_authentication_disable_smart_card_authentication**
> host_active_directory_authentication_disable_smart_card_authentication(mo_id)

Disables console authentication using a local smart card and reader. 

Disables console authentication using a local smart card and reader.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Disables console authentication using a local smart card and reader. 
        api_instance.host_active_directory_authentication_disable_smart_card_authentication(mo_id)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_disable_smart_card_authentication: %s\n" % e)
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
**500** | ***ActiveDirectoryFault***: if the active directory client could not be reconfigured.  ***HostConfigFault***: if the host configuration prevents smart card authentication from being disabled.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_enable_smart_card_authentication**
> host_active_directory_authentication_enable_smart_card_authentication(mo_id)

Enables console authentication using a local smart card and reader. 

Enables console authentication using a local smart card and reader.  To take effect this feature requires an active domain membership to a domain with users configured to authenticate using smart cards.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Enables console authentication using a local smart card and reader. 
        api_instance.host_active_directory_authentication_enable_smart_card_authentication(mo_id)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_enable_smart_card_authentication: %s\n" % e)
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
**500** | ***ActiveDirectoryFault***: if the active directory client could not be reconfigured.  ***HostConfigFault***: if the host configuration prevents smart card authentication from being enabled.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_get_info**
> HostAuthenticationStoreInfo host_active_directory_authentication_get_info(mo_id)

Information about the authentication store. 

Information about the authentication store.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_authentication_store_info import HostAuthenticationStoreInfo
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about the authentication store. 
        api_response = api_instance.host_active_directory_authentication_get_info(mo_id)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostAuthenticationStoreInfo**](HostAuthenticationStoreInfo.md)

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

# **host_active_directory_authentication_import_certificate_for_cam_task**
> ManagedObjectReference host_active_directory_authentication_import_certificate_for_cam_task(mo_id, import_certificate_for_cam_request_type)

Import the CAM server's certificate to the local store of vmwauth. 

Import the CAM server's certificate to the local store of vmwauth.  The certificate should have already been uploaded to ESXi file system.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.import_certificate_for_cam_request_type import ImportCertificateForCAMRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    import_certificate_for_cam_request_type = vmware_vi.ImportCertificateForCAMRequestType() # ImportCertificateForCAMRequestType | 

    try:
        # Import the CAM server's certificate to the local store of vmwauth. 
        api_response = api_instance.host_active_directory_authentication_import_certificate_for_cam_task(mo_id, import_certificate_for_cam_request_type)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_import_certificate_for_cam_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_import_certificate_for_cam_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **import_certificate_for_cam_request_type** | [**ImportCertificateForCAMRequestType**](ImportCertificateForCAMRequestType.md)|  | 

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
**500** | ***FileNotFound***: if the certificate file does not exist  ***InvalidCAMServer***: if camServer is not a valid IP address  ***ActiveDirectoryFault***: for any problem that is not handled with a more specific fault.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_install_smart_card_trust_anchor**
> host_active_directory_authentication_install_smart_card_trust_anchor(mo_id, install_smart_card_trust_anchor_request_type)

Install a trust anchor certificate for smart card authentication. 

Install a trust anchor certificate for smart card authentication.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.install_smart_card_trust_anchor_request_type import InstallSmartCardTrustAnchorRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    install_smart_card_trust_anchor_request_type = vmware_vi.InstallSmartCardTrustAnchorRequestType() # InstallSmartCardTrustAnchorRequestType | 

    try:
        # Install a trust anchor certificate for smart card authentication. 
        api_instance.host_active_directory_authentication_install_smart_card_trust_anchor(mo_id, install_smart_card_trust_anchor_request_type)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_install_smart_card_trust_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **install_smart_card_trust_anchor_request_type** | [**InstallSmartCardTrustAnchorRequestType**](InstallSmartCardTrustAnchorRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if the host configuration prevents the certificate from being installed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_join_domain_task**
> ManagedObjectReference host_active_directory_authentication_join_domain_task(mo_id, join_domain_request_type)

Adds the host to an Active Directory domain. 

Adds the host to an Active Directory domain.  If the *HostAuthenticationStoreInfo*.*HostAuthenticationStoreInfo.enabled* property is <code>True</code> (accessed through the <code>info</code> property), the host has joined a domain. The vSphere API will throw the <code>InvalidState</code> fault if you try to add a host to a domain when the host has already joined a domain.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.join_domain_request_type import JoinDomainRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    join_domain_request_type = vmware_vi.JoinDomainRequestType() # JoinDomainRequestType | 

    try:
        # Adds the host to an Active Directory domain. 
        api_response = api_instance.host_active_directory_authentication_join_domain_task(mo_id, join_domain_request_type)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_join_domain_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_join_domain_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **join_domain_request_type** | [**JoinDomainRequestType**](JoinDomainRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host has already joined a domain.  ***BlockedByFirewall***: if ports needed by the join operation are blocked by the firewall.  ***HostConfigFault***: if the host configuration prevents the join operation from succeeding.  ***InvalidLogin***: if &lt;code&gt;userName&lt;/code&gt; and &lt;code&gt;password&lt;/code&gt; are not valid user credentials.  ***DomainNotFound***: if the domain controller for &lt;code&gt;domainName&lt;/code&gt; cannot be reached.  ***NoPermissionOnAD***: if &lt;code&gt;userName&lt;/code&gt; has no right to add hosts to the domain.  ***InvalidHostName***: if the domain part of the host&#39;s FQDN doesn&#39;t match the domain being joined.  ***ClockSkew***: if the clocks of the host and the domain controller differ by more than the allowed amount of time.  ***ActiveDirectoryFault***: for any problem that is not handled with a more specific fault.  ***TaskInProgress***: if the *HostActiveDirectoryAuthentication* object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_join_domain_with_cam_task**
> ManagedObjectReference host_active_directory_authentication_join_domain_with_cam_task(mo_id, join_domain_with_cam_request_type)

Adds the host to an Active Directory domain through CAM service. 

Adds the host to an Active Directory domain through CAM service.  If the *HostAuthenticationStoreInfo*.*HostAuthenticationStoreInfo.enabled* property is <code>True</code> (accessed through the <code>info</code> property), the host has joined a domain. The vSphere API will throw the <code>InvalidState</code> fault if you try to add a host to a domain when the host has already joined a domain.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.join_domain_with_cam_request_type import JoinDomainWithCAMRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    join_domain_with_cam_request_type = vmware_vi.JoinDomainWithCAMRequestType() # JoinDomainWithCAMRequestType | 

    try:
        # Adds the host to an Active Directory domain through CAM service. 
        api_response = api_instance.host_active_directory_authentication_join_domain_with_cam_task(mo_id, join_domain_with_cam_request_type)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_join_domain_with_cam_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_join_domain_with_cam_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **join_domain_with_cam_request_type** | [**JoinDomainWithCAMRequestType**](JoinDomainWithCAMRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host has already joined a domain.  ***BlockedByFirewall***: if ports needed by the join operation are blocked by the firewall.  ***HostConfigFault***: if the host configuration prevents the join operation from succeeding.  ***DomainNotFound***: if the domain controller for &lt;code&gt;domainName&lt;/code&gt; cannot be reached.  ***InvalidHostName***: if the domain part of the host&#39;s FQDN doesn&#39;t match the domain being joined.  ***ClockSkew***: if the clocks of the host and the domain controller differ by more than the allowed amount of time.  ***InvalidCAMServer***: if camServer is not a valid IP address, or if camServer is not accessible.  ***InvalidCAMCertificate***: if the certificate of the given CAM server cannot be verified.  ***CAMServerRefusedConnection***: if the specified CAM server is not reachable, or if the server denied access.  ***ActiveDirectoryFault***: for any problem that is not handled with a more specific fault.  ***TaskInProgress***: if the *HostActiveDirectoryAuthentication* object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_leave_current_domain_task**
> ManagedObjectReference host_active_directory_authentication_leave_current_domain_task(mo_id, leave_current_domain_request_type)

Removes the host from the Active Directory domain to which it belongs. 

Removes the host from the Active Directory domain to which it belongs.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.leave_current_domain_request_type import LeaveCurrentDomainRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    leave_current_domain_request_type = vmware_vi.LeaveCurrentDomainRequestType() # LeaveCurrentDomainRequestType | 

    try:
        # Removes the host from the Active Directory domain to which it belongs. 
        api_response = api_instance.host_active_directory_authentication_leave_current_domain_task(mo_id, leave_current_domain_request_type)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_leave_current_domain_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_leave_current_domain_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **leave_current_domain_request_type** | [**LeaveCurrentDomainRequestType**](LeaveCurrentDomainRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host is not in a domain or there are active permissions for Active Directory users.  ***NonADUserRequired***: only non Active Directory users can initiate the leave domain operation.  ***AuthMinimumAdminPermission***: if this change would leave the system with no Administrator permission on the root node.  ***ActiveDirectoryFault***: for any problem that is not handled with a specific fault.  ***TaskInProgress***: if the ActiveDirectoryAuthentication object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_list_smart_card_trust_anchors**
> List[str] host_active_directory_authentication_list_smart_card_trust_anchors(mo_id)

Lists installed trust anchor certificates for smart card authentication. 

Lists installed trust anchor certificates for smart card authentication.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Lists installed trust anchor certificates for smart card authentication. 
        api_response = api_instance.host_active_directory_authentication_list_smart_card_trust_anchors(mo_id)
        print("The response of HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_list_smart_card_trust_anchors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_list_smart_card_trust_anchors: %s\n" % e)
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
**200** | SSL certificates of trusted CAs in PEM format.  |  -  |
**500** | ***HostConfigFault***: if the host configuration prevents the certificates from being listed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_remove_smart_card_trust_anchor**
> host_active_directory_authentication_remove_smart_card_trust_anchor(mo_id, remove_smart_card_trust_anchor_request_type)

Remove a smart card trust anchor certificate from the system. 

Deprecated please remove by fingerprint/digest instead.  Remove a smart card trust anchor certificate from the system.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_smart_card_trust_anchor_request_type import RemoveSmartCardTrustAnchorRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_smart_card_trust_anchor_request_type = vmware_vi.RemoveSmartCardTrustAnchorRequestType() # RemoveSmartCardTrustAnchorRequestType | 

    try:
        # Remove a smart card trust anchor certificate from the system. 
        api_instance.host_active_directory_authentication_remove_smart_card_trust_anchor(mo_id, remove_smart_card_trust_anchor_request_type)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_remove_smart_card_trust_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_smart_card_trust_anchor_request_type** | [**RemoveSmartCardTrustAnchorRequestType**](RemoveSmartCardTrustAnchorRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if the host configuration prevents the certificate from being removed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint**
> host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint(mo_id, remove_smart_card_trust_anchor_by_fingerprint_request_type)

Remove a smart card trust anchor certificate from the system by fingerprint. 

Remove a smart card trust anchor certificate from the system by fingerprint.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_smart_card_trust_anchor_by_fingerprint_request_type import RemoveSmartCardTrustAnchorByFingerprintRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_smart_card_trust_anchor_by_fingerprint_request_type = vmware_vi.RemoveSmartCardTrustAnchorByFingerprintRequestType() # RemoveSmartCardTrustAnchorByFingerprintRequestType | 

    try:
        # Remove a smart card trust anchor certificate from the system by fingerprint. 
        api_instance.host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint(mo_id, remove_smart_card_trust_anchor_by_fingerprint_request_type)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_remove_smart_card_trust_anchor_by_fingerprint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_smart_card_trust_anchor_by_fingerprint_request_type** | [**RemoveSmartCardTrustAnchorByFingerprintRequestType**](RemoveSmartCardTrustAnchorByFingerprintRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if the host configuration prevents the certificate from being removed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_active_directory_authentication_replace_smart_card_trust_anchors**
> host_active_directory_authentication_replace_smart_card_trust_anchors(mo_id, replace_smart_card_trust_anchors_request_type)

Replace the trust anchor certificates for smart card authentication. 

Replace the trust anchor certificates for smart card authentication.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.AuthenticationStore 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.replace_smart_card_trust_anchors_request_type import ReplaceSmartCardTrustAnchorsRequestType
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
    api_instance = vmware_vi.HostActiveDirectoryAuthenticationApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    replace_smart_card_trust_anchors_request_type = vmware_vi.ReplaceSmartCardTrustAnchorsRequestType() # ReplaceSmartCardTrustAnchorsRequestType | 

    try:
        # Replace the trust anchor certificates for smart card authentication. 
        api_instance.host_active_directory_authentication_replace_smart_card_trust_anchors(mo_id, replace_smart_card_trust_anchors_request_type)
    except Exception as e:
        print("Exception when calling HostActiveDirectoryAuthenticationApi->host_active_directory_authentication_replace_smart_card_trust_anchors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **replace_smart_card_trust_anchors_request_type** | [**ReplaceSmartCardTrustAnchorsRequestType**](ReplaceSmartCardTrustAnchorsRequestType.md)|  | 

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

