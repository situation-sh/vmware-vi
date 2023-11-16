# vmware_vi.HostSpecificationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_specification_manager_delete_host_specification**](HostSpecificationManagerApi.md#host_specification_manager_delete_host_specification) | **POST** /HostSpecificationManager/{moId}/DeleteHostSpecification | Delete the host specification of the specified host. 
[**host_specification_manager_delete_host_sub_specification**](HostSpecificationManagerApi.md#host_specification_manager_delete_host_sub_specification) | **POST** /HostSpecificationManager/{moId}/DeleteHostSubSpecification | Delete the host sub specification specified by the provided &lt;code&gt; subSpecname&lt;/code&gt; of the specified host. 
[**host_specification_manager_host_spec_get_updated_hosts**](HostSpecificationManagerApi.md#host_specification_manager_host_spec_get_updated_hosts) | **POST** /HostSpecificationManager/{moId}/HostSpecGetUpdatedHosts | Query the hosts whose specification was updated in the specified time period. 
[**host_specification_manager_retrieve_host_specification**](HostSpecificationManagerApi.md#host_specification_manager_retrieve_host_specification) | **POST** /HostSpecificationManager/{moId}/RetrieveHostSpecification | Retrieve the host specification. 
[**host_specification_manager_update_host_specification**](HostSpecificationManagerApi.md#host_specification_manager_update_host_specification) | **POST** /HostSpecificationManager/{moId}/UpdateHostSpecification | Update the host specification with the provided copy. 
[**host_specification_manager_update_host_sub_specification**](HostSpecificationManagerApi.md#host_specification_manager_update_host_sub_specification) | **POST** /HostSpecificationManager/{moId}/UpdateHostSubSpecification | Update the host specification with the provided host sub specification. 


# **host_specification_manager_delete_host_specification**
> host_specification_manager_delete_host_specification(mo_id, delete_host_specification_request_type)

Delete the host specification of the specified host. 

Delete the host specification of the specified host.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_host_specification_request_type import DeleteHostSpecificationRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_host_specification_request_type = vmware_vi.DeleteHostSpecificationRequestType() # DeleteHostSpecificationRequestType | 

    try:
        # Delete the host specification of the specified host. 
        api_instance.host_specification_manager_delete_host_specification(mo_id, delete_host_specification_request_type)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_delete_host_specification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_host_specification_request_type** | [**DeleteHostSpecificationRequestType**](DeleteHostSpecificationRequestType.md)|  | 

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
**500** | ***HostSpecificationOperationFailed***: If the method fails when delete the spec.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_specification_manager_delete_host_sub_specification**
> host_specification_manager_delete_host_sub_specification(mo_id, delete_host_sub_specification_request_type)

Delete the host sub specification specified by the provided <code> subSpecname</code> of the specified host. 

Delete the host sub specification specified by the provided <code> subSpecname</code> of the specified host.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_host_sub_specification_request_type import DeleteHostSubSpecificationRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_host_sub_specification_request_type = vmware_vi.DeleteHostSubSpecificationRequestType() # DeleteHostSubSpecificationRequestType | 

    try:
        # Delete the host sub specification specified by the provided <code> subSpecname</code> of the specified host. 
        api_instance.host_specification_manager_delete_host_sub_specification(mo_id, delete_host_sub_specification_request_type)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_delete_host_sub_specification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_host_sub_specification_request_type** | [**DeleteHostSubSpecificationRequestType**](DeleteHostSubSpecificationRequestType.md)|  | 

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
**500** | ***HostSpecificationOperationFailed***: If the method fails when delete the sub spec.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_specification_manager_host_spec_get_updated_hosts**
> List[ManagedObjectReference] host_specification_manager_host_spec_get_updated_hosts(mo_id, host_spec_get_updated_hosts_request_type)

Query the hosts whose specification was updated in the specified time period. 

Query the hosts whose specification was updated in the specified time period.  When the <code>startChangeID</code> isn't provided, it will return all the host updated before the <code>endChangeID</code>. When the <code>endChangeID</code> isn't provided, it will return all the hosts updated after <code>startChangeID</code>. If both aren't provided, all hosts having host spec will be returned. The format of the change ID is defined at *HostSpecification.changeID*.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_spec_get_updated_hosts_request_type import HostSpecGetUpdatedHostsRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_spec_get_updated_hosts_request_type = vmware_vi.HostSpecGetUpdatedHostsRequestType() # HostSpecGetUpdatedHostsRequestType | 

    try:
        # Query the hosts whose specification was updated in the specified time period. 
        api_response = api_instance.host_specification_manager_host_spec_get_updated_hosts(mo_id, host_spec_get_updated_hosts_request_type)
        print("The response of HostSpecificationManagerApi->host_specification_manager_host_spec_get_updated_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_host_spec_get_updated_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_spec_get_updated_hosts_request_type** | [**HostSpecGetUpdatedHostsRequestType**](HostSpecGetUpdatedHostsRequestType.md)|  | 

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
**200** | The queried host list.  Refers instances of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_specification_manager_retrieve_host_specification**
> HostSpecification host_specification_manager_retrieve_host_specification(mo_id, retrieve_host_specification_request_type)

Retrieve the host specification. 

Retrieve the host specification.  When the parameter <code>fromHost</code> is <code>true</code>, the host specification is retrieved from the host; otherwise, it is from the host specification \"database\" for this manager. When retrieved from host, the copy in host specification \"database\" will be updated. On success, it will fire a <code>HostSpecificationChangedEvent</code>.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_specification import HostSpecification
from vmware_vi.models.retrieve_host_specification_request_type import RetrieveHostSpecificationRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_host_specification_request_type = vmware_vi.RetrieveHostSpecificationRequestType() # RetrieveHostSpecificationRequestType | 

    try:
        # Retrieve the host specification. 
        api_response = api_instance.host_specification_manager_retrieve_host_specification(mo_id, retrieve_host_specification_request_type)
        print("The response of HostSpecificationManagerApi->host_specification_manager_retrieve_host_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_retrieve_host_specification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_host_specification_request_type** | [**RetrieveHostSpecificationRequestType**](RetrieveHostSpecificationRequestType.md)|  | 

### Return type

[**HostSpecification**](HostSpecification.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The host specification of the specified host.  |  -  |
**500** | ***HostSpecificationOperationFailed***: If the method fails when retrieve from host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_specification_manager_update_host_specification**
> host_specification_manager_update_host_specification(mo_id, update_host_specification_request_type)

Update the host specification with the provided copy. 

Update the host specification with the provided copy.  If there is no host specification for the host, create the host specification for this host in the host specification \"database\"; otherwise, update the host specification with the provided. *HostSpecification* object. On success, it will fire a <code>HostSpecificationChangedEvent</code>.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_host_specification_request_type import UpdateHostSpecificationRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_host_specification_request_type = vmware_vi.UpdateHostSpecificationRequestType() # UpdateHostSpecificationRequestType | 

    try:
        # Update the host specification with the provided copy. 
        api_instance.host_specification_manager_update_host_specification(mo_id, update_host_specification_request_type)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_update_host_specification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_host_specification_request_type** | [**UpdateHostSpecificationRequestType**](UpdateHostSpecificationRequestType.md)|  | 

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
**500** | ***HostSpecificationOperationFailed***: If the method fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_specification_manager_update_host_sub_specification**
> host_specification_manager_update_host_sub_specification(mo_id, update_host_sub_specification_request_type)

Update the host specification with the provided host sub specification. 

Update the host specification with the provided host sub specification.  If there is no host specification for the host, create the host specification, which contains only the provided host sub specification, for this host; otherwise, add or update the host specification with the provided *HostSubSpecification* object. This method provides a way to incrementally build the host specification. On success, it will fire a <code>HostSpecificationChangedEvent</code>.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Profile.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_host_sub_specification_request_type import UpdateHostSubSpecificationRequestType
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
    api_instance = vmware_vi.HostSpecificationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_host_sub_specification_request_type = vmware_vi.UpdateHostSubSpecificationRequestType() # UpdateHostSubSpecificationRequestType | 

    try:
        # Update the host specification with the provided host sub specification. 
        api_instance.host_specification_manager_update_host_sub_specification(mo_id, update_host_sub_specification_request_type)
    except Exception as e:
        print("Exception when calling HostSpecificationManagerApi->host_specification_manager_update_host_sub_specification: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_host_sub_specification_request_type** | [**UpdateHostSubSpecificationRequestType**](UpdateHostSubSpecificationRequestType.md)|  | 

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
**500** | ***HostSpecificationOperationFailed***: If the method fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

