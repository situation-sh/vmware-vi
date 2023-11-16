# vmware_vi.HttpNfcLeaseApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**http_nfc_lease_get_capabilities**](HttpNfcLeaseApi.md#http_nfc_lease_get_capabilities) | **GET** /HttpNfcLease/{moId}/capabilities | Current supported capabilities by this lease See *HttpNfcLeaseCapabilities* 
[**http_nfc_lease_get_error**](HttpNfcLeaseApi.md#http_nfc_lease_get_error) | **GET** /HttpNfcLease/{moId}/error | If the lease is in the error state, this property contains the error that caused the lease to be aborted. 
[**http_nfc_lease_get_info**](HttpNfcLeaseApi.md#http_nfc_lease_get_info) | **GET** /HttpNfcLease/{moId}/info | Provides information on the objects contained in this lease. 
[**http_nfc_lease_get_initialize_progress**](HttpNfcLeaseApi.md#http_nfc_lease_get_initialize_progress) | **GET** /HttpNfcLease/{moId}/initializeProgress | Provides progress information (0-100 percent) for the initializing state of the lease. 
[**http_nfc_lease_get_mode**](HttpNfcLeaseApi.md#http_nfc_lease_get_mode) | **GET** /HttpNfcLease/{moId}/mode | Current mode of the lease. 
[**http_nfc_lease_get_state**](HttpNfcLeaseApi.md#http_nfc_lease_get_state) | **GET** /HttpNfcLease/{moId}/state | The current state of the lease. 
[**http_nfc_lease_get_transfer_progress**](HttpNfcLeaseApi.md#http_nfc_lease_get_transfer_progress) | **GET** /HttpNfcLease/{moId}/transferProgress | Provides progress information (0-100 percent) for current transfer. 
[**http_nfc_lease_http_nfc_lease_abort**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_abort) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseAbort | Aborts the import/export and releases this lease. 
[**http_nfc_lease_http_nfc_lease_complete**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_complete) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseComplete | Completes the import/export and releases this lease. 
[**http_nfc_lease_http_nfc_lease_get_manifest**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_get_manifest) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseGetManifest | Gets the download manifest for this lease. 
[**http_nfc_lease_http_nfc_lease_probe_urls**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_probe_urls) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseProbeUrls | Perform a series of validations on the target host to see if it can succesfully perform PullFromUrls. 
[**http_nfc_lease_http_nfc_lease_progress**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_progress) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseProgress | Sets the disk up/download progress, and renews this lease. 
[**http_nfc_lease_http_nfc_lease_pull_from_urls_task**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_pull_from_urls_task) | **POST** /HttpNfcLease/{moId}/HttpNfcLeasePullFromUrls_Task | Upgrades current lease from push to pull mode. 
[**http_nfc_lease_http_nfc_lease_set_manifest_checksum_type**](HttpNfcLeaseApi.md#http_nfc_lease_http_nfc_lease_set_manifest_checksum_type) | **POST** /HttpNfcLease/{moId}/HttpNfcLeaseSetManifestChecksumType | Sets desired checksum algorithm per each file that will be returned in ManifestEntry. 


# **http_nfc_lease_get_capabilities**
> HttpNfcLeaseCapabilities http_nfc_lease_get_capabilities(mo_id)

Current supported capabilities by this lease See *HttpNfcLeaseCapabilities* 

Current supported capabilities by this lease See *HttpNfcLeaseCapabilities*  ***Since:*** vSphere API 6.7 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_capabilities import HttpNfcLeaseCapabilities
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current supported capabilities by this lease See *HttpNfcLeaseCapabilities* 
        api_response = api_instance.http_nfc_lease_get_capabilities(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_capabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HttpNfcLeaseCapabilities**](HttpNfcLeaseCapabilities.md)

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

# **http_nfc_lease_get_error**
> MethodFault http_nfc_lease_get_error(mo_id)

If the lease is in the error state, this property contains the error that caused the lease to be aborted. 

If the lease is in the error state, this property contains the error that caused the lease to be aborted.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.method_fault import MethodFault
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # If the lease is in the error state, this property contains the error that caused the lease to be aborted. 
        api_response = api_instance.http_nfc_lease_get_error(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_error: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**MethodFault**](MethodFault.md)

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

# **http_nfc_lease_get_info**
> HttpNfcLeaseInfo http_nfc_lease_get_info(mo_id)

Provides information on the objects contained in this lease. 

Provides information on the objects contained in this lease.  The info property is only valid when the lease is in the ready state.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_info import HttpNfcLeaseInfo
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Provides information on the objects contained in this lease. 
        api_response = api_instance.http_nfc_lease_get_info(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HttpNfcLeaseInfo**](HttpNfcLeaseInfo.md)

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

# **http_nfc_lease_get_initialize_progress**
> int http_nfc_lease_get_initialize_progress(mo_id)

Provides progress information (0-100 percent) for the initializing state of the lease. 

Provides progress information (0-100 percent) for the initializing state of the lease.  Clients can use this to track overall progress.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Provides progress information (0-100 percent) for the initializing state of the lease. 
        api_response = api_instance.http_nfc_lease_get_initialize_progress(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_initialize_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_initialize_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**int**

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

# **http_nfc_lease_get_mode**
> str http_nfc_lease_get_mode(mo_id)

Current mode of the lease. 

Current mode of the lease.  See *HttpNfcLeaseMode_enum* for possible values.  ***Since:*** vSphere API 6.7 

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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current mode of the lease. 
        api_response = api_instance.http_nfc_lease_get_mode(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_mode: %s\n" % e)
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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_get_state**
> HttpNfcLeaseStateEnum http_nfc_lease_get_state(mo_id)

The current state of the lease. 

The current state of the lease.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_state_enum import HttpNfcLeaseStateEnum
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The current state of the lease. 
        api_response = api_instance.http_nfc_lease_get_state(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HttpNfcLeaseStateEnum**](HttpNfcLeaseStateEnum.md)

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

# **http_nfc_lease_get_transfer_progress**
> int http_nfc_lease_get_transfer_progress(mo_id)

Provides progress information (0-100 percent) for current transfer. 

Provides progress information (0-100 percent) for current transfer.  Transfer covers download, upload and pull scenario. Can be externally updated by progress method.  ***Since:*** vSphere API 6.7 

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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Provides progress information (0-100 percent) for current transfer. 
        api_response = api_instance.http_nfc_lease_get_transfer_progress(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_get_transfer_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_get_transfer_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**int**

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

# **http_nfc_lease_http_nfc_lease_abort**
> http_nfc_lease_http_nfc_lease_abort(mo_id, http_nfc_lease_abort_request_type)

Aborts the import/export and releases this lease. 

Aborts the import/export and releases this lease.  Operations on the objects contained in this lease will no longer be blocked. After calling this method, this lease will no longer be valid.  Clients should call this method if an error occurs while accessing the disks, or if the operation is cancelled. The client can report the cause of the abort to other clients listening on the task with the fault parameter.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_abort_request_type import HttpNfcLeaseAbortRequestType
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    http_nfc_lease_abort_request_type = vmware_vi.HttpNfcLeaseAbortRequestType() # HttpNfcLeaseAbortRequestType | 

    try:
        # Aborts the import/export and releases this lease. 
        api_instance.http_nfc_lease_http_nfc_lease_abort(mo_id, http_nfc_lease_abort_request_type)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_abort: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **http_nfc_lease_abort_request_type** | [**HttpNfcLeaseAbortRequestType**](HttpNfcLeaseAbortRequestType.md)|  | 

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
**500** | ***Timedout***: if the lease has timed out before this call.  ***InvalidState***: if the lease has already been aborted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_complete**
> http_nfc_lease_http_nfc_lease_complete(mo_id)

Completes the import/export and releases this lease. 

Completes the import/export and releases this lease.  Operations on the objects contained in this lease will no longer be blocked. After calling this method, this lease will no longer be valid.  Clients should call this method when they are done accessing the disks for the *VirtualMachine*s in this lease. The status of the corresponding task will be set to success.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Completes the import/export and releases this lease. 
        api_instance.http_nfc_lease_http_nfc_lease_complete(mo_id)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_complete: %s\n" % e)
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
**500** | ***Timedout***: if the lease has timed out before this call.  ***InvalidState***: if the lease has already been completed or aborted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_get_manifest**
> List[HttpNfcLeaseManifestEntry] http_nfc_lease_http_nfc_lease_get_manifest(mo_id)

Gets the download manifest for this lease. 

Gets the download manifest for this lease.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_manifest_entry import HttpNfcLeaseManifestEntry
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Gets the download manifest for this lease. 
        api_response = api_instance.http_nfc_lease_http_nfc_lease_get_manifest(mo_id)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_get_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_get_manifest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HttpNfcLeaseManifestEntry]**](HttpNfcLeaseManifestEntry.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_probe_urls**
> List[HttpNfcLeaseProbeResult] http_nfc_lease_http_nfc_lease_probe_urls(mo_id, http_nfc_lease_probe_urls_request_type)

Perform a series of validations on the target host to see if it can succesfully perform PullFromUrls. 

Perform a series of validations on the target host to see if it can succesfully perform PullFromUrls.  ***Since:*** vSphere API 7.0.2.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_probe_result import HttpNfcLeaseProbeResult
from vmware_vi.models.http_nfc_lease_probe_urls_request_type import HttpNfcLeaseProbeUrlsRequestType
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    http_nfc_lease_probe_urls_request_type = vmware_vi.HttpNfcLeaseProbeUrlsRequestType() # HttpNfcLeaseProbeUrlsRequestType | 

    try:
        # Perform a series of validations on the target host to see if it can succesfully perform PullFromUrls. 
        api_response = api_instance.http_nfc_lease_http_nfc_lease_probe_urls(mo_id, http_nfc_lease_probe_urls_request_type)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_probe_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_probe_urls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **http_nfc_lease_probe_urls_request_type** | [**HttpNfcLeaseProbeUrlsRequestType**](HttpNfcLeaseProbeUrlsRequestType.md)|  | 

### Return type

[**List[HttpNfcLeaseProbeResult]**](HttpNfcLeaseProbeResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidArgument***: if no source files are provided.  ***InvalidState***: if the lease has already been aborted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_progress**
> http_nfc_lease_http_nfc_lease_progress(mo_id, http_nfc_lease_progress_request_type)

Sets the disk up/download progress, and renews this lease. 

Sets the disk up/download progress, and renews this lease.  A lease will time out automatically after a while. If the client wishes to continue using it, for example if it is not done accessing the disks, this method must be called periodically.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_progress_request_type import HttpNfcLeaseProgressRequestType
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    http_nfc_lease_progress_request_type = vmware_vi.HttpNfcLeaseProgressRequestType() # HttpNfcLeaseProgressRequestType | 

    try:
        # Sets the disk up/download progress, and renews this lease. 
        api_instance.http_nfc_lease_http_nfc_lease_progress(mo_id, http_nfc_lease_progress_request_type)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_progress: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **http_nfc_lease_progress_request_type** | [**HttpNfcLeaseProgressRequestType**](HttpNfcLeaseProgressRequestType.md)|  | 

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
**500** | ***Timedout***: if the lease has timed out or vSphere has not detected data transfer progress.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_pull_from_urls_task**
> ManagedObjectReference http_nfc_lease_http_nfc_lease_pull_from_urls_task(mo_id, http_nfc_lease_pull_from_urls_request_type)

Upgrades current lease from push to pull mode. 

Upgrades current lease from push to pull mode.  ***Since:*** vSphere API 6.7 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_pull_from_urls_request_type import HttpNfcLeasePullFromUrlsRequestType
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    http_nfc_lease_pull_from_urls_request_type = vmware_vi.HttpNfcLeasePullFromUrlsRequestType() # HttpNfcLeasePullFromUrlsRequestType | 

    try:
        # Upgrades current lease from push to pull mode. 
        api_response = api_instance.http_nfc_lease_http_nfc_lease_pull_from_urls_task(mo_id, http_nfc_lease_pull_from_urls_request_type)
        print("The response of HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_pull_from_urls_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_pull_from_urls_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **http_nfc_lease_pull_from_urls_request_type** | [**HttpNfcLeasePullFromUrlsRequestType**](HttpNfcLeasePullFromUrlsRequestType.md)|  | 

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
**500** | ***InvalidState***: if the lease has already been aborted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_nfc_lease_http_nfc_lease_set_manifest_checksum_type**
> http_nfc_lease_http_nfc_lease_set_manifest_checksum_type(mo_id, http_nfc_lease_set_manifest_checksum_type_request_type)

Sets desired checksum algorithm per each file that will be returned in ManifestEntry. 

Sets desired checksum algorithm per each file that will be returned in ManifestEntry.  Should be set before any transfer starts.  ***Since:*** vSphere API 6.7 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.http_nfc_lease_set_manifest_checksum_type_request_type import HttpNfcLeaseSetManifestChecksumTypeRequestType
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
    api_instance = vmware_vi.HttpNfcLeaseApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    http_nfc_lease_set_manifest_checksum_type_request_type = vmware_vi.HttpNfcLeaseSetManifestChecksumTypeRequestType() # HttpNfcLeaseSetManifestChecksumTypeRequestType | 

    try:
        # Sets desired checksum algorithm per each file that will be returned in ManifestEntry. 
        api_instance.http_nfc_lease_http_nfc_lease_set_manifest_checksum_type(mo_id, http_nfc_lease_set_manifest_checksum_type_request_type)
    except Exception as e:
        print("Exception when calling HttpNfcLeaseApi->http_nfc_lease_http_nfc_lease_set_manifest_checksum_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **http_nfc_lease_set_manifest_checksum_type_request_type** | [**HttpNfcLeaseSetManifestChecksumTypeRequestType**](HttpNfcLeaseSetManifestChecksumTypeRequestType.md)|  | 

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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

