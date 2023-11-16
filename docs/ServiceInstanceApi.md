# vmware_vi.ServiceInstanceApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_instance_current_time**](ServiceInstanceApi.md#service_instance_current_time) | **POST** /ServiceInstance/{moId}/CurrentTime | Returns the current time on the server. 
[**service_instance_get_capability**](ServiceInstanceApi.md#service_instance_get_capability) | **GET** /ServiceInstance/{moId}/capability | API-wide capabilities. 
[**service_instance_get_content**](ServiceInstanceApi.md#service_instance_get_content) | **GET** /ServiceInstance/{moId}/content | The properties of the ServiceInstance managed object. 
[**service_instance_get_server_clock**](ServiceInstanceApi.md#service_instance_get_server_clock) | **GET** /ServiceInstance/{moId}/serverClock | Contains the time most recently obtained from the server. 
[**service_instance_query_v_motion_compatibility**](ServiceInstanceApi.md#service_instance_query_v_motion_compatibility) | **POST** /ServiceInstance/{moId}/QueryVMotionCompatibility | Investigates the general VMotion compatibility of a virtual machine with a set of hosts. 
[**service_instance_retrieve_product_components**](ServiceInstanceApi.md#service_instance_retrieve_product_components) | **POST** /ServiceInstance/{moId}/RetrieveProductComponents | Component information for bundled products 
[**service_instance_retrieve_service_content**](ServiceInstanceApi.md#service_instance_retrieve_service_content) | **POST** /ServiceInstance/{moId}/RetrieveServiceContent | Retrieves the properties of the service instance. 
[**service_instance_validate_migration**](ServiceInstanceApi.md#service_instance_validate_migration) | **POST** /ServiceInstance/{moId}/ValidateMigration | Checks the validity of a set of proposed migrations. 


# **service_instance_current_time**
> datetime service_instance_current_time(mo_id)

Returns the current time on the server. 

Returns the current time on the server.  To monitor non-linear time changes, use the *serverClock* property.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns the current time on the server. 
        api_response = api_instance.service_instance_current_time(mo_id)
        print("The response of ServiceInstanceApi->service_instance_current_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_current_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The date and time on the server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_instance_get_capability**
> Capability service_instance_get_capability(mo_id)

API-wide capabilities. 

API-wide capabilities.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.capability import Capability
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # API-wide capabilities. 
        api_response = api_instance.service_instance_get_capability(mo_id)
        print("The response of ServiceInstanceApi->service_instance_get_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_get_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**Capability**](Capability.md)

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

# **service_instance_get_content**
> ServiceContent service_instance_get_content(mo_id)

The properties of the ServiceInstance managed object. 

The properties of the ServiceInstance managed object.  The content property is identical to the return value from the *ServiceInstance.RetrieveServiceContent* method.  Use the content property with the *PropertyCollector* to perform inventory traversal that includes the ServiceInstance. (In the absence of a content property, a traversal that encounters the *ServiceInstance* would require calling the *ServiceInstance.RetrieveServiceContent* method, and then invoking a second traversal to continue.)  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.service_content import ServiceContent
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The properties of the ServiceInstance managed object. 
        api_response = api_instance.service_instance_get_content(mo_id)
        print("The response of ServiceInstanceApi->service_instance_get_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_get_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ServiceContent**](ServiceContent.md)

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

# **service_instance_get_server_clock**
> datetime service_instance_get_server_clock(mo_id)

Contains the time most recently obtained from the server. 

Contains the time most recently obtained from the server.  The time is not necessarily current. This property is intended for use with the PropertyCollector *PropertyCollector.WaitForUpdates* method. The PropertyCollector will provide notification if some event occurs that changes the server clock time in a non-linear fashion.  You should not rely on the serverClock property to get the current time on the server; instead, use the *ServiceInstance.CurrentTime* method.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Contains the time most recently obtained from the server. 
        api_response = api_instance.service_instance_get_server_clock(mo_id)
        print("The response of ServiceInstanceApi->service_instance_get_server_clock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_get_server_clock: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**datetime**

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

# **service_instance_query_v_motion_compatibility**
> List[HostVMotionCompatibility] service_instance_query_v_motion_compatibility(mo_id, query_v_motion_compatibility_request_type)

Investigates the general VMotion compatibility of a virtual machine with a set of hosts. 

Deprecated as of vSphere API 4.0, use *VirtualMachineProvisioningChecker.QueryVMotionCompatibilityEx_Task* instead.  Investigates the general VMotion compatibility of a virtual machine with a set of hosts.  The virtual machine may be in any power state. Hosts may be in any connection state and also may be in maintenance mode.  ***Required privileges:*** Resource.QueryVMotion 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_motion_compatibility import HostVMotionCompatibility
from vmware_vi.models.query_v_motion_compatibility_request_type import QueryVMotionCompatibilityRequestType
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_v_motion_compatibility_request_type = vmware_vi.QueryVMotionCompatibilityRequestType() # QueryVMotionCompatibilityRequestType | 

    try:
        # Investigates the general VMotion compatibility of a virtual machine with a set of hosts. 
        api_response = api_instance.service_instance_query_v_motion_compatibility(mo_id, query_v_motion_compatibility_request_type)
        print("The response of ServiceInstanceApi->service_instance_query_v_motion_compatibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_query_v_motion_compatibility: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_v_motion_compatibility_request_type** | [**QueryVMotionCompatibilityRequestType**](QueryVMotionCompatibilityRequestType.md)|  | 

### Return type

[**List[HostVMotionCompatibility]**](HostVMotionCompatibility.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array where each element, associated with one of the input hosts, specifies which of the requested compatibility types applies to that host. If an input host has never been connected and therefore has no information available for determining its compatibility, it is omitted from the return list.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_instance_retrieve_product_components**
> List[ProductComponentInfo] service_instance_retrieve_product_components(mo_id)

Component information for bundled products 

Component information for bundled products  ***Since:*** VI API 2.5  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.product_component_info import ProductComponentInfo
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Component information for bundled products 
        api_response = api_instance.service_instance_retrieve_product_components(mo_id)
        print("The response of ServiceInstanceApi->service_instance_retrieve_product_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_retrieve_product_components: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ProductComponentInfo]**](ProductComponentInfo.md)

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

# **service_instance_retrieve_service_content**
> ServiceContent service_instance_retrieve_service_content(mo_id)

Retrieves the properties of the service instance. 

Retrieves the properties of the service instance.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.service_content import ServiceContent
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieves the properties of the service instance. 
        api_response = api_instance.service_instance_retrieve_service_content(mo_id)
        print("The response of ServiceInstanceApi->service_instance_retrieve_service_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_retrieve_service_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ServiceContent**](ServiceContent.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties belonging to the service instance, including various object managers.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_instance_validate_migration**
> List[Event] service_instance_validate_migration(mo_id, validate_migration_request_type)

Checks the validity of a set of proposed migrations. 

Deprecated as of vSphere API 4.0, use *VirtualMachineProvisioningChecker* instead.  Checks the validity of a set of proposed migrations.  A migration is the act of changing the assigned execution host of a virtual machine, which can result from invoking *VirtualMachine.MigrateVM_Task* or *VirtualMachine.RelocateVM_Task*.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
from vmware_vi.models.validate_migration_request_type import ValidateMigrationRequestType
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
    api_instance = vmware_vi.ServiceInstanceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    validate_migration_request_type = vmware_vi.ValidateMigrationRequestType() # ValidateMigrationRequestType | 

    try:
        # Checks the validity of a set of proposed migrations. 
        api_response = api_instance.service_instance_validate_migration(mo_id, validate_migration_request_type)
        print("The response of ServiceInstanceApi->service_instance_validate_migration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceInstanceApi->service_instance_validate_migration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **validate_migration_request_type** | [**ValidateMigrationRequestType**](ValidateMigrationRequestType.md)|  | 

### Return type

[**List[Event]**](Event.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of events that describe the warnings or errors that would apply if the proposed set of migrations were executed.  |  -  |
**500** | ***InvalidArgument***: if the target host(s) and target pool for a migration are not associated with the same compute resource, or if the host parameter is left unset when the target pool is associated with a non-DRS cluster.  ***InvalidPowerState***: if the state argument is set and at least one of the specified virtual machines is not in that power state.  ***NoActiveHostInCluster***: if a target host is not specified and a cluster associated with a target pool does not contain at least one potential target host. A host must be connected and not in maintenance mode in order to be considered as a potential target host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

