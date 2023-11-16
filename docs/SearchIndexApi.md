# vmware_vi.SearchIndexApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_index_find_all_by_dns_name**](SearchIndexApi.md#search_index_find_all_by_dns_name) | **POST** /SearchIndex/{moId}/FindAllByDnsName | Finds all virtual machines or hosts by DNS name. 
[**search_index_find_all_by_ip**](SearchIndexApi.md#search_index_find_all_by_ip) | **POST** /SearchIndex/{moId}/FindAllByIp | Finds all virtual machines or hosts by IP address, where the IP address is in dot-decimal notation. 
[**search_index_find_all_by_uuid**](SearchIndexApi.md#search_index_find_all_by_uuid) | **POST** /SearchIndex/{moId}/FindAllByUuid | Finds all virtual machines or hosts by UUID. 
[**search_index_find_by_datastore_path**](SearchIndexApi.md#search_index_find_by_datastore_path) | **POST** /SearchIndex/{moId}/FindByDatastorePath | Finds a virtual machine by its location on a datastore. 
[**search_index_find_by_dns_name**](SearchIndexApi.md#search_index_find_by_dns_name) | **POST** /SearchIndex/{moId}/FindByDnsName | Finds a virtual machine or host by DNS name. 
[**search_index_find_by_inventory_path**](SearchIndexApi.md#search_index_find_by_inventory_path) | **POST** /SearchIndex/{moId}/FindByInventoryPath | Finds a managed entity based on its location in the inventory. 
[**search_index_find_by_ip**](SearchIndexApi.md#search_index_find_by_ip) | **POST** /SearchIndex/{moId}/FindByIp | Finds a virtual machine or host by IP address, where the IP address is in dot-decimal notation. 
[**search_index_find_by_uuid**](SearchIndexApi.md#search_index_find_by_uuid) | **POST** /SearchIndex/{moId}/FindByUuid | Finds a virtual machine or host by BIOS or instance UUID. 
[**search_index_find_child**](SearchIndexApi.md#search_index_find_child) | **POST** /SearchIndex/{moId}/FindChild | Finds a particular child based on a managed entity name. 


# **search_index_find_all_by_dns_name**
> List[ManagedObjectReference] search_index_find_all_by_dns_name(mo_id, find_all_by_dns_name_request_type)

Finds all virtual machines or hosts by DNS name. 

Finds all virtual machines or hosts by DNS name.  The DNS name for a virtual machine is the one returned from VMware tools, *GuestInfo.hostName*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_all_by_dns_name_request_type import FindAllByDnsNameRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_all_by_dns_name_request_type = vmware_vi.FindAllByDnsNameRequestType() # FindAllByDnsNameRequestType | 

    try:
        # Finds all virtual machines or hosts by DNS name. 
        api_response = api_instance.search_index_find_all_by_dns_name(mo_id, find_all_by_dns_name_request_type)
        print("The response of SearchIndexApi->search_index_find_all_by_dns_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_all_by_dns_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_all_by_dns_name_request_type** | [**FindAllByDnsNameRequestType**](FindAllByDnsNameRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all virtual machines or hosts that are found. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_all_by_ip**
> List[ManagedObjectReference] search_index_find_all_by_ip(mo_id, find_all_by_ip_request_type)

Finds all virtual machines or hosts by IP address, where the IP address is in dot-decimal notation. 

Finds all virtual machines or hosts by IP address, where the IP address is in dot-decimal notation.  For example, 10.17.12.12. The IP address for a virtual machine is the one returned from VMware tools, *GuestInfo.ipAddress*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_all_by_ip_request_type import FindAllByIpRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_all_by_ip_request_type = vmware_vi.FindAllByIpRequestType() # FindAllByIpRequestType | 

    try:
        # Finds all virtual machines or hosts by IP address, where the IP address is in dot-decimal notation. 
        api_response = api_instance.search_index_find_all_by_ip(mo_id, find_all_by_ip_request_type)
        print("The response of SearchIndexApi->search_index_find_all_by_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_all_by_ip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_all_by_ip_request_type** | [**FindAllByIpRequestType**](FindAllByIpRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all virtual machines or hosts that are found. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_all_by_uuid**
> List[ManagedObjectReference] search_index_find_all_by_uuid(mo_id, find_all_by_uuid_request_type)

Finds all virtual machines or hosts by UUID. 

Finds all virtual machines or hosts by UUID.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_all_by_uuid_request_type import FindAllByUuidRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_all_by_uuid_request_type = vmware_vi.FindAllByUuidRequestType() # FindAllByUuidRequestType | 

    try:
        # Finds all virtual machines or hosts by UUID. 
        api_response = api_instance.search_index_find_all_by_uuid(mo_id, find_all_by_uuid_request_type)
        print("The response of SearchIndexApi->search_index_find_all_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_all_by_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_all_by_uuid_request_type** | [**FindAllByUuidRequestType**](FindAllByUuidRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all virtual machines or hosts that are matching with the given UUID. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_by_datastore_path**
> ManagedObjectReference search_index_find_by_datastore_path(mo_id, find_by_datastore_path_request_type)

Finds a virtual machine by its location on a datastore. 

Finds a virtual machine by its location on a datastore.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_by_datastore_path_request_type import FindByDatastorePathRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_by_datastore_path_request_type = vmware_vi.FindByDatastorePathRequestType() # FindByDatastorePathRequestType | 

    try:
        # Finds a virtual machine by its location on a datastore. 
        api_response = api_instance.search_index_find_by_datastore_path(mo_id, find_by_datastore_path_request_type)
        print("The response of SearchIndexApi->search_index_find_by_datastore_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_by_datastore_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_by_datastore_path_request_type** | [**FindByDatastorePathRequestType**](FindByDatastorePathRequestType.md)|  | 

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
**200** | The virtual machine that is found. If no virtual machine is found, null is returned. Only a single entity is returned, even if there are multiple matches.  Refers instance of *VirtualMachine*.  |  -  |
**500** | ***InvalidDatastore***: if a datastore has not been specified in the path or if the specified datastore does not exist on the specified datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_by_dns_name**
> ManagedObjectReference search_index_find_by_dns_name(mo_id, find_by_dns_name_request_type)

Finds a virtual machine or host by DNS name. 

Finds a virtual machine or host by DNS name.  The DNS name for a virtual machine is the one returned from VMware tools, *GuestInfo.hostName*.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_by_dns_name_request_type import FindByDnsNameRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_by_dns_name_request_type = vmware_vi.FindByDnsNameRequestType() # FindByDnsNameRequestType | 

    try:
        # Finds a virtual machine or host by DNS name. 
        api_response = api_instance.search_index_find_by_dns_name(mo_id, find_by_dns_name_request_type)
        print("The response of SearchIndexApi->search_index_find_by_dns_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_by_dns_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_by_dns_name_request_type** | [**FindByDnsNameRequestType**](FindByDnsNameRequestType.md)|  | 

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
**200** | The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches.  Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_by_inventory_path**
> ManagedObjectReference search_index_find_by_inventory_path(mo_id, find_by_inventory_path_request_type)

Finds a managed entity based on its location in the inventory. 

Finds a managed entity based on its location in the inventory.  The path is separated by slashes ('/'). For example, a path should be of the form \"My Folder/My Datacenter/vm/Discovered VM/VM1\". A leading slash or trailing slash is ignored. Thus, the following paths all represents the same object: \"a/b\", \"/a/b\", \"a/b/\", and '/a/b/'. Slashes in names must be represented using %2f, following the standard URL syntax. Any object in the inventory can be retrieved using this method, including resource pools and hosts.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_by_inventory_path_request_type import FindByInventoryPathRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_by_inventory_path_request_type = vmware_vi.FindByInventoryPathRequestType() # FindByInventoryPathRequestType | 

    try:
        # Finds a managed entity based on its location in the inventory. 
        api_response = api_instance.search_index_find_by_inventory_path(mo_id, find_by_inventory_path_request_type)
        print("The response of SearchIndexApi->search_index_find_by_inventory_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_by_inventory_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_by_inventory_path_request_type** | [**FindByInventoryPathRequestType**](FindByInventoryPathRequestType.md)|  | 

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
**200** | The managed entity that is found. If no match is found, null is returned.  Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_by_ip**
> ManagedObjectReference search_index_find_by_ip(mo_id, find_by_ip_request_type)

Finds a virtual machine or host by IP address, where the IP address is in dot-decimal notation. 

Finds a virtual machine or host by IP address, where the IP address is in dot-decimal notation.  For example, 10.17.12.12. The IP address for a virtual machine is the one returned from VMware tools, *GuestInfo.ipAddress*.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_by_ip_request_type import FindByIpRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_by_ip_request_type = vmware_vi.FindByIpRequestType() # FindByIpRequestType | 

    try:
        # Finds a virtual machine or host by IP address, where the IP address is in dot-decimal notation. 
        api_response = api_instance.search_index_find_by_ip(mo_id, find_by_ip_request_type)
        print("The response of SearchIndexApi->search_index_find_by_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_by_ip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_by_ip_request_type** | [**FindByIpRequestType**](FindByIpRequestType.md)|  | 

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
**200** | The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches. If called directly on an ESX server with vmSearch set to false, returns the host managed entity if the address matches any of the Console OS IP addresses.  Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_by_uuid**
> ManagedObjectReference search_index_find_by_uuid(mo_id, find_by_uuid_request_type)

Finds a virtual machine or host by BIOS or instance UUID. 

Finds a virtual machine or host by BIOS or instance UUID.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_by_uuid_request_type import FindByUuidRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_by_uuid_request_type = vmware_vi.FindByUuidRequestType() # FindByUuidRequestType | 

    try:
        # Finds a virtual machine or host by BIOS or instance UUID. 
        api_response = api_instance.search_index_find_by_uuid(mo_id, find_by_uuid_request_type)
        print("The response of SearchIndexApi->search_index_find_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_by_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_by_uuid_request_type** | [**FindByUuidRequestType**](FindByUuidRequestType.md)|  | 

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
**200** | The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches.  Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index_find_child**
> ManagedObjectReference search_index_find_child(mo_id, find_child_request_type)

Finds a particular child based on a managed entity name. 

Finds a particular child based on a managed entity name.  This only searches the immediate children of a managed entity. For a *Datacenter*, the host and vm folders are considered children. For a *ComputeResource*, the hosts and root *ResourcePool* are considered children.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.find_child_request_type import FindChildRequestType
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
    api_instance = vmware_vi.SearchIndexApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_child_request_type = vmware_vi.FindChildRequestType() # FindChildRequestType | 

    try:
        # Finds a particular child based on a managed entity name. 
        api_response = api_instance.search_index_find_child(mo_id, find_child_request_type)
        print("The response of SearchIndexApi->search_index_find_child:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchIndexApi->search_index_find_child: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_child_request_type** | [**FindChildRequestType**](FindChildRequestType.md)|  | 

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
**200** | The managed entity that is found, or null if no match is found.  Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

