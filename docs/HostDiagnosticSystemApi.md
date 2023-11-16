# vmware_vi.HostDiagnosticSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_diagnostic_system_create_diagnostic_partition**](HostDiagnosticSystemApi.md#host_diagnostic_system_create_diagnostic_partition) | **POST** /HostDiagnosticSystem/{moId}/CreateDiagnosticPartition | Creates a diagnostic partition according to the provided create specification. 
[**host_diagnostic_system_get_active_partition**](HostDiagnosticSystemApi.md#host_diagnostic_system_get_active_partition) | **GET** /HostDiagnosticSystem/{moId}/activePartition | The currently active diagnostic partition. 
[**host_diagnostic_system_query_available_partition**](HostDiagnosticSystemApi.md#host_diagnostic_system_query_available_partition) | **POST** /HostDiagnosticSystem/{moId}/QueryAvailablePartition | Retrieves a list of available diagnostic partitions. 
[**host_diagnostic_system_query_partition_create_desc**](HostDiagnosticSystemApi.md#host_diagnostic_system_query_partition_create_desc) | **POST** /HostDiagnosticSystem/{moId}/QueryPartitionCreateDesc | For a disk, query for the diagnostic partition creation description. 
[**host_diagnostic_system_query_partition_create_options**](HostDiagnosticSystemApi.md#host_diagnostic_system_query_partition_create_options) | **POST** /HostDiagnosticSystem/{moId}/QueryPartitionCreateOptions | Retrieves a list of disks that can be used to contain a diagnostic partition. 
[**host_diagnostic_system_select_active_partition**](HostDiagnosticSystemApi.md#host_diagnostic_system_select_active_partition) | **POST** /HostDiagnosticSystem/{moId}/SelectActivePartition | Changes the active diagnostic partition to a different partition. 


# **host_diagnostic_system_create_diagnostic_partition**
> host_diagnostic_system_create_diagnostic_partition(mo_id, create_diagnostic_partition_request_type)

Creates a diagnostic partition according to the provided create specification. 

Creates a diagnostic partition according to the provided create specification.  On success, this method will create the partition and make the partition the active diagnostic partition if specified. On failure, the diagnostic partition may exist but may not be active if the partition was supposed to be made active.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_diagnostic_partition_request_type import CreateDiagnosticPartitionRequestType
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_diagnostic_partition_request_type = vmware_vi.CreateDiagnosticPartitionRequestType() # CreateDiagnosticPartitionRequestType | 

    try:
        # Creates a diagnostic partition according to the provided create specification. 
        api_instance.host_diagnostic_system_create_diagnostic_partition(mo_id, create_diagnostic_partition_request_type)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_create_diagnostic_partition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_diagnostic_partition_request_type** | [**CreateDiagnosticPartitionRequestType**](CreateDiagnosticPartitionRequestType.md)|  | 

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
**500** | ***NotSupported***: if the host is not an ESX Server.  ***NotFound***: if the specified disk cannot be found.  ***InvalidArgument***: if an invalid storage type is specified or the specified disk is unable to accommodate a new diagnostic partition.  ***HostConfigFault***: on some internal failure while trying to create the diagnostic partition or to activate the diagnostic partition.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_diagnostic_system_get_active_partition**
> HostDiagnosticPartition host_diagnostic_system_get_active_partition(mo_id)

The currently active diagnostic partition. 

The currently active diagnostic partition. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_diagnostic_partition import HostDiagnosticPartition
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The currently active diagnostic partition. 
        api_response = api_instance.host_diagnostic_system_get_active_partition(mo_id)
        print("The response of HostDiagnosticSystemApi->host_diagnostic_system_get_active_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_get_active_partition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostDiagnosticPartition**](HostDiagnosticPartition.md)

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

# **host_diagnostic_system_query_available_partition**
> List[HostDiagnosticPartition] host_diagnostic_system_query_available_partition(mo_id)

Retrieves a list of available diagnostic partitions. 

Retrieves a list of available diagnostic partitions.  The server will provide the list in order of preference. In general, local diagnostic partitions are better than shared diagnostic partitions because of the impossibility of multiple servers sharing the same partition. The most preferred diagnostic partition will be first in the array.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_diagnostic_partition import HostDiagnosticPartition
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieves a list of available diagnostic partitions. 
        api_response = api_instance.host_diagnostic_system_query_available_partition(mo_id)
        print("The response of HostDiagnosticSystemApi->host_diagnostic_system_query_available_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_query_available_partition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostDiagnosticPartition]**](HostDiagnosticPartition.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotSupported***: if the host is not an ESX Server.  ***HostConfigFault***: on some internal failure while setting the active partition.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_diagnostic_system_query_partition_create_desc**
> HostDiagnosticPartitionCreateDescription host_diagnostic_system_query_partition_create_desc(mo_id, query_partition_create_desc_request_type)

For a disk, query for the diagnostic partition creation description. 

For a disk, query for the diagnostic partition creation description.  The description details how the diagnostic partition will be created on the disk and provides a creation specification that is needed to invoke the create operation.  See also *HostScsiDisk*, *ScsiLun.uuid*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_diagnostic_partition_create_description import HostDiagnosticPartitionCreateDescription
from vmware_vi.models.query_partition_create_desc_request_type import QueryPartitionCreateDescRequestType
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_partition_create_desc_request_type = vmware_vi.QueryPartitionCreateDescRequestType() # QueryPartitionCreateDescRequestType | 

    try:
        # For a disk, query for the diagnostic partition creation description. 
        api_response = api_instance.host_diagnostic_system_query_partition_create_desc(mo_id, query_partition_create_desc_request_type)
        print("The response of HostDiagnosticSystemApi->host_diagnostic_system_query_partition_create_desc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_query_partition_create_desc: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_partition_create_desc_request_type** | [**QueryPartitionCreateDescRequestType**](QueryPartitionCreateDescRequestType.md)|  | 

### Return type

[**HostDiagnosticPartitionCreateDescription**](HostDiagnosticPartitionCreateDescription.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotSupported***: if the host is not an ESX Server.  ***NotFound***: if the specified disk cannot be found.  ***InvalidArgument***: if an invalid storage type is specified or the specified disk is unable to accommodate a new diagnostic partition.  ***HostConfigFault***: on some internal failure while trying to query information about the disk.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_diagnostic_system_query_partition_create_options**
> List[HostDiagnosticPartitionCreateOption] host_diagnostic_system_query_partition_create_options(mo_id, query_partition_create_options_request_type)

Retrieves a list of disks that can be used to contain a diagnostic partition. 

Retrieves a list of disks that can be used to contain a diagnostic partition.  This list will contain disks that have sufficient space to contain a diagnostic partition of the specific type.  The choices will be returned in the order that is most preferable as determined by the system.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_diagnostic_partition_create_option import HostDiagnosticPartitionCreateOption
from vmware_vi.models.query_partition_create_options_request_type import QueryPartitionCreateOptionsRequestType
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_partition_create_options_request_type = vmware_vi.QueryPartitionCreateOptionsRequestType() # QueryPartitionCreateOptionsRequestType | 

    try:
        # Retrieves a list of disks that can be used to contain a diagnostic partition. 
        api_response = api_instance.host_diagnostic_system_query_partition_create_options(mo_id, query_partition_create_options_request_type)
        print("The response of HostDiagnosticSystemApi->host_diagnostic_system_query_partition_create_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_query_partition_create_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_partition_create_options_request_type** | [**QueryPartitionCreateOptionsRequestType**](QueryPartitionCreateOptionsRequestType.md)|  | 

### Return type

[**List[HostDiagnosticPartitionCreateOption]**](HostDiagnosticPartitionCreateOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotSupported***: if the host is not an ESX Server.  ***InvalidArgument***: if an invalid storage type is specified.  ***HostConfigFault***: on some internal failure while querying the create options.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_diagnostic_system_select_active_partition**
> host_diagnostic_system_select_active_partition(mo_id, select_active_partition_request_type)

Changes the active diagnostic partition to a different partition. 

Changes the active diagnostic partition to a different partition.  Setting a NULL partition will result in unsetting the diagnostic partition.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.select_active_partition_request_type import SelectActivePartitionRequestType
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
    api_instance = vmware_vi.HostDiagnosticSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    select_active_partition_request_type = vmware_vi.SelectActivePartitionRequestType() # SelectActivePartitionRequestType | 

    try:
        # Changes the active diagnostic partition to a different partition. 
        api_instance.host_diagnostic_system_select_active_partition(mo_id, select_active_partition_request_type)
    except Exception as e:
        print("Exception when calling HostDiagnosticSystemApi->host_diagnostic_system_select_active_partition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **select_active_partition_request_type** | [**SelectActivePartitionRequestType**](SelectActivePartitionRequestType.md)|  | 

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
**500** | ***NotSupported***: if the host is not an ESX Server.  ***NotFound***: if the diagnostic partition does not exist.  ***InvalidArgument***: if the partition is not a diagnostic partition.  ***HostConfigFault***: on some internal failure while selecting the active partition.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

