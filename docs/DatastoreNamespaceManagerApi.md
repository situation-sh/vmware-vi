# vmware_vi.DatastoreNamespaceManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datastore_namespace_manager_convert_namespace_path_to_uuid_path**](DatastoreNamespaceManagerApi.md#datastore_namespace_manager_convert_namespace_path_to_uuid_path) | **POST** /DatastoreNamespaceManager/{moId}/ConvertNamespacePathToUuidPath | Convert the namespace path to the namespace UUID path. 
[**datastore_namespace_manager_create_directory**](DatastoreNamespaceManagerApi.md#datastore_namespace_manager_create_directory) | **POST** /DatastoreNamespaceManager/{moId}/CreateDirectory | Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy. 
[**datastore_namespace_manager_delete_directory**](DatastoreNamespaceManagerApi.md#datastore_namespace_manager_delete_directory) | **POST** /DatastoreNamespaceManager/{moId}/DeleteDirectory | Deletes the given top-level directory from a datastore. 
[**datastore_namespace_manager_increase_directory_size**](DatastoreNamespaceManagerApi.md#datastore_namespace_manager_increase_directory_size) | **POST** /DatastoreNamespaceManager/{moId}/IncreaseDirectorySize | Increase size of the given top-level directory to the given size on vSAN backed object storage. 
[**datastore_namespace_manager_query_directory_info**](DatastoreNamespaceManagerApi.md#datastore_namespace_manager_query_directory_info) | **POST** /DatastoreNamespaceManager/{moId}/QueryDirectoryInfo | Query directory information of the given top-level directory on vSAN backed object storage. 


# **datastore_namespace_manager_convert_namespace_path_to_uuid_path**
> str datastore_namespace_manager_convert_namespace_path_to_uuid_path(mo_id, convert_namespace_path_to_uuid_path_request_type)

Convert the namespace path to the namespace UUID path. 

Convert the namespace path to the namespace UUID path.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.convert_namespace_path_to_uuid_path_request_type import ConvertNamespacePathToUuidPathRequestType
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
    api_instance = vmware_vi.DatastoreNamespaceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    convert_namespace_path_to_uuid_path_request_type = vmware_vi.ConvertNamespacePathToUuidPathRequestType() # ConvertNamespacePathToUuidPathRequestType | 

    try:
        # Convert the namespace path to the namespace UUID path. 
        api_response = api_instance.datastore_namespace_manager_convert_namespace_path_to_uuid_path(mo_id, convert_namespace_path_to_uuid_path_request_type)
        print("The response of DatastoreNamespaceManagerApi->datastore_namespace_manager_convert_namespace_path_to_uuid_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatastoreNamespaceManagerApi->datastore_namespace_manager_convert_namespace_path_to_uuid_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **convert_namespace_path_to_uuid_path_request_type** | [**ConvertNamespacePathToUuidPathRequestType**](ConvertNamespacePathToUuidPathRequestType.md)|  | 

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
**200** | the URL path with namespace object UUID, of the form &gt; \\[ds://\\]/vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-uuid_\\]/... &gt;  |  -  |
**500** | ***InvalidDatastore***: if the given datastore is not supported by the DatastoreNamespaceManager  ***InvalidDatastorePath***: if the given path is not a top-level directory  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datastore_namespace_manager_create_directory**
> str datastore_namespace_manager_create_directory(mo_id, create_directory_request_type)

Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy. 

Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy.  The optional given display name hint may be used by the underlying storage system for user display purposes, but it may not be relied upon for future directory references.  Clients must use the returned stable path for future directory references.  See also *DatastoreNamespaceManager.DeleteDirectory*.  ***Since:*** vSphere API 5.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_directory_request_type import CreateDirectoryRequestType
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
    api_instance = vmware_vi.DatastoreNamespaceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_directory_request_type = vmware_vi.CreateDirectoryRequestType() # CreateDirectoryRequestType | 

    try:
        # Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy. 
        api_response = api_instance.datastore_namespace_manager_create_directory(mo_id, create_directory_request_type)
        print("The response of DatastoreNamespaceManagerApi->datastore_namespace_manager_create_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatastoreNamespaceManagerApi->datastore_namespace_manager_create_directory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_directory_request_type** | [**CreateDirectoryRequestType**](CreateDirectoryRequestType.md)|  | 

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
**200** | a stable vmfs path which may be used for future reference of the created directory, of the form &gt; /vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-uuid_\\] &gt;  |  -  |
**500** | ***CannotCreateFile***: if a general system error occurred while creating directory on the datastore  ***FileAlreadyExists***: if the given directory already exists  ***InvalidDatastore***: if the given datastore is not supported by the DatastoreNamespaceManage  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datastore_namespace_manager_delete_directory**
> datastore_namespace_manager_delete_directory(mo_id, delete_directory_request_type)

Deletes the given top-level directory from a datastore. 

Deletes the given top-level directory from a datastore.  The top-level directory must be a full path of the form > /vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-uuid_\\] >   as returned by *DatastoreNamespaceManager.CreateDirectory*.  Requires Datastore.Config privilege on the datastore.  See also *DatastoreNamespaceManager.CreateDirectory*.  ***Since:*** vSphere API 5.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_directory_request_type import DeleteDirectoryRequestType
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
    api_instance = vmware_vi.DatastoreNamespaceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_directory_request_type = vmware_vi.DeleteDirectoryRequestType() # DeleteDirectoryRequestType | 

    try:
        # Deletes the given top-level directory from a datastore. 
        api_instance.datastore_namespace_manager_delete_directory(mo_id, delete_directory_request_type)
    except Exception as e:
        print("Exception when calling DatastoreNamespaceManagerApi->datastore_namespace_manager_delete_directory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_directory_request_type** | [**DeleteDirectoryRequestType**](DeleteDirectoryRequestType.md)|  | 

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
**500** | ***FileNotFound***: if the given directory can not be found  ***FileFault***: if a generic system error happened.  ***InvalidDatastore***: if the given datastore is not supported by the DatastoreNamespaceManager  ***InvalidDatastorePath***: if the given path is not a top-level directory  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datastore_namespace_manager_increase_directory_size**
> datastore_namespace_manager_increase_directory_size(mo_id, increase_directory_size_request_type)

Increase size of the given top-level directory to the given size on vSAN backed object storage. 

Increase size of the given top-level directory to the given size on vSAN backed object storage.  The top-level directory must be a full path in the form > /vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-uuid_\\] >   as returned by *DatastoreNamespaceManager.CreateDirectory*.  Requires Datastore.Config privilege on the datastore.  See also *DatastoreNamespaceManager.CreateDirectory*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.increase_directory_size_request_type import IncreaseDirectorySizeRequestType
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
    api_instance = vmware_vi.DatastoreNamespaceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    increase_directory_size_request_type = vmware_vi.IncreaseDirectorySizeRequestType() # IncreaseDirectorySizeRequestType | 

    try:
        # Increase size of the given top-level directory to the given size on vSAN backed object storage. 
        api_instance.datastore_namespace_manager_increase_directory_size(mo_id, increase_directory_size_request_type)
    except Exception as e:
        print("Exception when calling DatastoreNamespaceManagerApi->datastore_namespace_manager_increase_directory_size: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **increase_directory_size_request_type** | [**IncreaseDirectorySizeRequestType**](IncreaseDirectorySizeRequestType.md)|  | 

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
**500** | ***FileFault***: if a generic system error happened  ***FileNotFound***: if the given directory can not be found  ***InvalidDatastore***: if the given datastore is not supported by the DatastoreNamespaceManager  ***NotSupported***: if resize is not supported on the directory  ***InvalidArgument***: if passed size is not valid  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datastore_namespace_manager_query_directory_info**
> DatastoreNamespaceManagerDirectoryInfo datastore_namespace_manager_query_directory_info(mo_id, query_directory_info_request_type)

Query directory information of the given top-level directory on vSAN backed object storage. 

Query directory information of the given top-level directory on vSAN backed object storage.  The top-level directory must be a full path in the form > /vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-uuid_\\] >   as returned by *DatastoreNamespaceManager.CreateDirectory*.  See also *DatastoreNamespaceManager.CreateDirectory*.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.datastore_namespace_manager_directory_info import DatastoreNamespaceManagerDirectoryInfo
from vmware_vi.models.query_directory_info_request_type import QueryDirectoryInfoRequestType
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
    api_instance = vmware_vi.DatastoreNamespaceManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_directory_info_request_type = vmware_vi.QueryDirectoryInfoRequestType() # QueryDirectoryInfoRequestType | 

    try:
        # Query directory information of the given top-level directory on vSAN backed object storage. 
        api_response = api_instance.datastore_namespace_manager_query_directory_info(mo_id, query_directory_info_request_type)
        print("The response of DatastoreNamespaceManagerApi->datastore_namespace_manager_query_directory_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatastoreNamespaceManagerApi->datastore_namespace_manager_query_directory_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_directory_info_request_type** | [**QueryDirectoryInfoRequestType**](QueryDirectoryInfoRequestType.md)|  | 

### Return type

[**DatastoreNamespaceManagerDirectoryInfo**](DatastoreNamespaceManagerDirectoryInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | directory information defined by *DatastoreNamespaceManagerDirectoryInfo*  |  -  |
**500** | ***FileFault***: if a generic system error happened  ***FileNotFound***: if the given directory can not be found  ***InvalidDatastore***: if the given datastore is not supported by the DatastoreNamespaceManager  ***NotSupported***: if query is not supported on the directory  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

