# vmware_vi.DiagnosticManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnostic_manager_browse_diagnostic_log**](DiagnosticManagerApi.md#diagnostic_manager_browse_diagnostic_log) | **POST** /DiagnosticManager/{moId}/BrowseDiagnosticLog | Returns part of a log file. 
[**diagnostic_manager_emit_syslog_mark**](DiagnosticManagerApi.md#diagnostic_manager_emit_syslog_mark) | **POST** /DiagnosticManager/{moId}/EmitSyslogMark | Issue a \&quot;mark\&quot; to syslog and the audit trail. 
[**diagnostic_manager_fetch_audit_records**](DiagnosticManagerApi.md#diagnostic_manager_fetch_audit_records) | **POST** /DiagnosticManager/{moId}/FetchAuditRecords | Retrieve audit records from their storage on the specified host. 
[**diagnostic_manager_generate_log_bundles_task**](DiagnosticManagerApi.md#diagnostic_manager_generate_log_bundles_task) | **POST** /DiagnosticManager/{moId}/GenerateLogBundles_Task | Instructs the server to generate diagnostic bundles. 
[**diagnostic_manager_query_descriptions**](DiagnosticManagerApi.md#diagnostic_manager_query_descriptions) | **POST** /DiagnosticManager/{moId}/QueryDescriptions | Returns a list of diagnostic files for a given system. 


# **diagnostic_manager_browse_diagnostic_log**
> DiagnosticManagerLogHeader diagnostic_manager_browse_diagnostic_log(mo_id, browse_diagnostic_log_request_type)

Returns part of a log file. 

Returns part of a log file.  Log entries are always returned chronologically, typically with the newest event last.  ***Required privileges:*** Global.Diagnostics 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.browse_diagnostic_log_request_type import BrowseDiagnosticLogRequestType
from vmware_vi.models.diagnostic_manager_log_header import DiagnosticManagerLogHeader
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
    api_instance = vmware_vi.DiagnosticManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    browse_diagnostic_log_request_type = vmware_vi.BrowseDiagnosticLogRequestType() # BrowseDiagnosticLogRequestType | 

    try:
        # Returns part of a log file. 
        api_response = api_instance.diagnostic_manager_browse_diagnostic_log(mo_id, browse_diagnostic_log_request_type)
        print("The response of DiagnosticManagerApi->diagnostic_manager_browse_diagnostic_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticManagerApi->diagnostic_manager_browse_diagnostic_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **browse_diagnostic_log_request_type** | [**BrowseDiagnosticLogRequestType**](BrowseDiagnosticLogRequestType.md)|  | 

### Return type

[**DiagnosticManagerLogHeader**](DiagnosticManagerLogHeader.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A LogHeader that includes the log lines. Sometimes fewer log lines are returned than were requested. For example, fewer lines are returned than expected if the client requests lines that do not exist or if the server limits the number of lines that it returns. If zero lines are returned, then the end of the log file may have been reached.  |  -  |
**500** | ***InvalidArgument***: if the key refers to a nonexistent log file or the log file is not of type \&quot;plain\&quot;.  ***CannotAccessFile***: if the key refers to a file that cannot be accessed at the present time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnostic_manager_emit_syslog_mark**
> diagnostic_manager_emit_syslog_mark(mo_id, emit_syslog_mark_request_type)

Issue a \"mark\" to syslog and the audit trail. 

Issue a \"mark\" to syslog and the audit trail.  The specified message string will be written to syslog and the audit trail. The \"mark\" audit record will contain the message string in its comment parameter.  ***Required privileges:*** Global.Diagnostics 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.emit_syslog_mark_request_type import EmitSyslogMarkRequestType
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
    api_instance = vmware_vi.DiagnosticManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    emit_syslog_mark_request_type = vmware_vi.EmitSyslogMarkRequestType() # EmitSyslogMarkRequestType | 

    try:
        # Issue a \"mark\" to syslog and the audit trail. 
        api_instance.diagnostic_manager_emit_syslog_mark(mo_id, emit_syslog_mark_request_type)
    except Exception as e:
        print("Exception when calling DiagnosticManagerApi->diagnostic_manager_emit_syslog_mark: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **emit_syslog_mark_request_type** | [**EmitSyslogMarkRequestType**](EmitSyslogMarkRequestType.md)|  | 

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

# **diagnostic_manager_fetch_audit_records**
> DiagnosticManagerAuditRecordResult diagnostic_manager_fetch_audit_records(mo_id, fetch_audit_records_request_type)

Retrieve audit records from their storage on the specified host. 

Retrieve audit records from their storage on the specified host.  Audit records are stored on the host in a (large) FIFO. The FIFO is continuously being written to due to system activities. It is the responsibility of the caller to issue reads fast enough to keep ahead of the write traffic.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Global.Diagnostics 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.diagnostic_manager_audit_record_result import DiagnosticManagerAuditRecordResult
from vmware_vi.models.fetch_audit_records_request_type import FetchAuditRecordsRequestType
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
    api_instance = vmware_vi.DiagnosticManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    fetch_audit_records_request_type = vmware_vi.FetchAuditRecordsRequestType() # FetchAuditRecordsRequestType | 

    try:
        # Retrieve audit records from their storage on the specified host. 
        api_response = api_instance.diagnostic_manager_fetch_audit_records(mo_id, fetch_audit_records_request_type)
        print("The response of DiagnosticManagerApi->diagnostic_manager_fetch_audit_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticManagerApi->diagnostic_manager_fetch_audit_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **fetch_audit_records_request_type** | [**FetchAuditRecordsRequestType**](FetchAuditRecordsRequestType.md)|  | 

### Return type

[**DiagnosticManagerAuditRecordResult**](DiagnosticManagerAuditRecordResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidState***: The reader has failed to keep up with the write data rate. Data has been lost. It is up to the caller to decide how to react to this. One possibility is to \&quot;start again from the beginning\&quot; with a call with no token.  ***SystemError***: One more more errors (on the host) have occurred. One or more error strings are available to detail the issues.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnostic_manager_generate_log_bundles_task**
> ManagedObjectReference diagnostic_manager_generate_log_bundles_task(mo_id, generate_log_bundles_request_type)

Instructs the server to generate diagnostic bundles. 

Deprecated since version 5.0 M/N it is recommended to use the CGI interface for the host bundles, use the address instead: `https://<<ESX_name>>/cgi-bin/vm-support.cgi` for the VC bundles, use `https://<<VC_name>>/appliance/support-bundle`  The caller can download the bundles using an HTTP GET operation for each returned URL. Bundles are usually available for at least 24 hours, but the caller should not assume that the returned URLs are valid indefinitely. Servers often automatically delete generated diagnostic bundles after some given period of time.  Instructs the server to generate diagnostic bundles.  A diagnostic bundle includes log files and other configuration information that can be used to investigate potential server issues. Virtual machine and guest operation system state is excluded from diagnostic bundles.  ***Required privileges:*** Global.Diagnostics 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.generate_log_bundles_request_type import GenerateLogBundlesRequestType
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
    api_instance = vmware_vi.DiagnosticManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    generate_log_bundles_request_type = vmware_vi.GenerateLogBundlesRequestType() # GenerateLogBundlesRequestType | 

    try:
        # Instructs the server to generate diagnostic bundles. 
        api_response = api_instance.diagnostic_manager_generate_log_bundles_task(mo_id, generate_log_bundles_request_type)
        print("The response of DiagnosticManagerApi->diagnostic_manager_generate_log_bundles_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticManagerApi->diagnostic_manager_generate_log_bundles_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **generate_log_bundles_request_type** | [**GenerateLogBundlesRequestType**](GenerateLogBundlesRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. Upon success, the *info.result* property in the *Task* contains a list of *DiagnosticManagerBundleInfo* objects for each diagnostic bundle that has been generated.  Refers instance of *Task*.  |  -  |
**500** | ***LogBundlingFailed***: if generation of support bundle failed.  ***TaskInProgress***: if there is a pending request to generate a support bundle.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnostic_manager_query_descriptions**
> List[DiagnosticManagerLogDescriptor] diagnostic_manager_query_descriptions(mo_id, query_descriptions_request_type)

Returns a list of diagnostic files for a given system. 

Returns a list of diagnostic files for a given system.  ***Required privileges:*** Global.Diagnostics 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.diagnostic_manager_log_descriptor import DiagnosticManagerLogDescriptor
from vmware_vi.models.query_descriptions_request_type import QueryDescriptionsRequestType
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
    api_instance = vmware_vi.DiagnosticManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_descriptions_request_type = vmware_vi.QueryDescriptionsRequestType() # QueryDescriptionsRequestType | 

    try:
        # Returns a list of diagnostic files for a given system. 
        api_response = api_instance.diagnostic_manager_query_descriptions(mo_id, query_descriptions_request_type)
        print("The response of DiagnosticManagerApi->diagnostic_manager_query_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticManagerApi->diagnostic_manager_query_descriptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_descriptions_request_type** | [**QueryDescriptionsRequestType**](QueryDescriptionsRequestType.md)|  | 

### Return type

[**List[DiagnosticManagerLogDescriptor]**](DiagnosticManagerLogDescriptor.md)

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

