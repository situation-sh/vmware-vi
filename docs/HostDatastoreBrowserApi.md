# vmware_vi.HostDatastoreBrowserApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_datastore_browser_delete_file**](HostDatastoreBrowserApi.md#host_datastore_browser_delete_file) | **POST** /HostDatastoreBrowser/{moId}/DeleteFile | Deletes the specified files from the datastore. 
[**host_datastore_browser_get_datastore**](HostDatastoreBrowserApi.md#host_datastore_browser_get_datastore) | **GET** /HostDatastoreBrowser/{moId}/datastore | Set of datastores that can be searched on this DatastoreBrowser. 
[**host_datastore_browser_get_supported_type**](HostDatastoreBrowserApi.md#host_datastore_browser_get_supported_type) | **GET** /HostDatastoreBrowser/{moId}/supportedType | The list of supported file types. 
[**host_datastore_browser_search_datastore_sub_folders_task**](HostDatastoreBrowserApi.md#host_datastore_browser_search_datastore_sub_folders_task) | **POST** /HostDatastoreBrowser/{moId}/SearchDatastoreSubFolders_Task | Returns the information for the files that match the given search criteria as a SearchResults\\[\\] object. 
[**host_datastore_browser_search_datastore_task**](HostDatastoreBrowserApi.md#host_datastore_browser_search_datastore_task) | **POST** /HostDatastoreBrowser/{moId}/SearchDatastore_Task | Returns the information for the files that match the given search criteria as a SearchResults object. 


# **host_datastore_browser_delete_file**
> host_datastore_browser_delete_file(mo_id, delete_file_request_type)

Deletes the specified files from the datastore. 

Deprecated as of VI API 2.5, use *FileManager.DeleteDatastoreFile_Task*.  Deletes the specified files from the datastore.  If a valid virtual disk file is specified, then all the components of the virtual disk are deleted.  ***Required privileges:*** Datastore.DeleteFile 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_file_request_type import DeleteFileRequestType
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
    api_instance = vmware_vi.HostDatastoreBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_file_request_type = vmware_vi.DeleteFileRequestType() # DeleteFileRequestType | 

    try:
        # Deletes the specified files from the datastore. 
        api_instance.host_datastore_browser_delete_file(mo_id, delete_file_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreBrowserApi->host_datastore_browser_delete_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_file_request_type** | [**DeleteFileRequestType**](DeleteFileRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: if the operation cannot be performed on the target datastores. Typically, a specific subclass of this exception is thrown.  ***FileNotFound***: if the file or folder specified by datastorePath is not found.  ***CannotDeleteFile***: if the delete operation on the file fails.  ***InvalidArgument***: if fileInfo is not a valid FileInfo type.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_browser_get_datastore**
> List[ManagedObjectReference] host_datastore_browser_get_datastore(mo_id)

Set of datastores that can be searched on this DatastoreBrowser. 

Set of datastores that can be searched on this DatastoreBrowser.  The list of datastores available to browse on this DatastoreBrowser is contextual information that depends on the object being browsed. If the host is being browsed, the host's datastores are used. If the Datacenter is being browsed, the Datacenter's list of datastores is used.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.HostDatastoreBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Set of datastores that can be searched on this DatastoreBrowser. 
        api_response = api_instance.host_datastore_browser_get_datastore(mo_id)
        print("The response of HostDatastoreBrowserApi->host_datastore_browser_get_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreBrowserApi->host_datastore_browser_get_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *Datastore*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_browser_get_supported_type**
> List[FileQuery] host_datastore_browser_get_supported_type(mo_id)

The list of supported file types. 

The list of supported file types.  The supported file types are represented as items in this list. For each supported file type, there is an object in the list whose dynamic type is one of the types derived from the *FileQuery* data object type. In general, the properties in this query type are not set.  Use the Query of the desired file type in the SearchSpec.query to indicate the desired file types.  This property is used by clients to determine what kinds of file types are supported. Clients should consult this list to avoid querying for types of virtual machine components that are not supported. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.file_query import FileQuery
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
    api_instance = vmware_vi.HostDatastoreBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of supported file types. 
        api_response = api_instance.host_datastore_browser_get_supported_type(mo_id)
        print("The response of HostDatastoreBrowserApi->host_datastore_browser_get_supported_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreBrowserApi->host_datastore_browser_get_supported_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[FileQuery]**](FileQuery.md)

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

# **host_datastore_browser_search_datastore_sub_folders_task**
> ManagedObjectReference host_datastore_browser_search_datastore_sub_folders_task(mo_id, search_datastore_sub_folders_request_type)

Returns the information for the files that match the given search criteria as a SearchResults\\[\\] object. 

Returns the information for the files that match the given search criteria as a SearchResults\\[\\] object.  Searches the folder specified by the datastore path and all subfolders. The Datastore.Browse privilege must be held on the datastore identified by the datastore path. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.search_datastore_sub_folders_request_type import SearchDatastoreSubFoldersRequestType
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
    api_instance = vmware_vi.HostDatastoreBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    search_datastore_sub_folders_request_type = vmware_vi.SearchDatastoreSubFoldersRequestType() # SearchDatastoreSubFoldersRequestType | 

    try:
        # Returns the information for the files that match the given search criteria as a SearchResults\\[\\] object. 
        api_response = api_instance.host_datastore_browser_search_datastore_sub_folders_task(mo_id, search_datastore_sub_folders_request_type)
        print("The response of HostDatastoreBrowserApi->host_datastore_browser_search_datastore_sub_folders_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreBrowserApi->host_datastore_browser_search_datastore_sub_folders_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **search_datastore_sub_folders_request_type** | [**SearchDatastoreSubFoldersRequestType**](SearchDatastoreSubFoldersRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostDatastoreBrowserSearchResults* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidDatastore***: if the operation cannot be performed on the target datastores. Typically, a specific subclass of this exception is thrown.  ***InvalidArgument***: if the SearchSpec contains duplicate file types.  ***FileNotFound***: if the file or folder specified by datastorePath is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_browser_search_datastore_task**
> ManagedObjectReference host_datastore_browser_search_datastore_task(mo_id, search_datastore_request_type)

Returns the information for the files that match the given search criteria as a SearchResults object. 

Returns the information for the files that match the given search criteria as a SearchResults object.  Searches only the folder specified by the datastore path. The Datastore.Browse privilege must be held on the datastore identified by the datastore path. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.search_datastore_request_type import SearchDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    search_datastore_request_type = vmware_vi.SearchDatastoreRequestType() # SearchDatastoreRequestType | 

    try:
        # Returns the information for the files that match the given search criteria as a SearchResults object. 
        api_response = api_instance.host_datastore_browser_search_datastore_task(mo_id, search_datastore_request_type)
        print("The response of HostDatastoreBrowserApi->host_datastore_browser_search_datastore_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreBrowserApi->host_datastore_browser_search_datastore_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **search_datastore_request_type** | [**SearchDatastoreRequestType**](SearchDatastoreRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostDatastoreBrowserSearchResults* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidDatastore***: if the operation cannot be performed on the target datastores. The server can throw InvalidDatastorePath to indicate a malformed datastorePath, or InaccessibleDatastore to indicate inaccessibility of the datastore.  ***InvalidArgument***: if the SearchSpec contains duplicate file types.  ***FileNotFound***: if the file or folder specified by datastorePath is not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

