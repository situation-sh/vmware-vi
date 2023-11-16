# vmware_vi.ClusterEVCManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_evc_manager_check_add_host_evc_task**](ClusterEVCManagerApi.md#cluster_evc_manager_check_add_host_evc_task) | **POST** /ClusterEVCManager/{moId}/CheckAddHostEvc_Task | Test the validity of adding a host into the managed cluster. 
[**cluster_evc_manager_check_configure_evc_mode_task**](ClusterEVCManagerApi.md#cluster_evc_manager_check_configure_evc_mode_task) | **POST** /ClusterEVCManager/{moId}/CheckConfigureEvcMode_Task | Test the validity of configuring an EVC mode on the managed cluster. 
[**cluster_evc_manager_configure_evc_mode_task**](ClusterEVCManagerApi.md#cluster_evc_manager_configure_evc_mode_task) | **POST** /ClusterEVCManager/{moId}/ConfigureEvcMode_Task | Set the EVC mode. 
[**cluster_evc_manager_disable_evc_mode_task**](ClusterEVCManagerApi.md#cluster_evc_manager_disable_evc_mode_task) | **POST** /ClusterEVCManager/{moId}/DisableEvcMode_Task | Disable EVC. 
[**cluster_evc_manager_get_available_field**](ClusterEVCManagerApi.md#cluster_evc_manager_get_available_field) | **GET** /ClusterEVCManager/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**cluster_evc_manager_get_evc_state**](ClusterEVCManagerApi.md#cluster_evc_manager_get_evc_state) | **GET** /ClusterEVCManager/{moId}/evcState | EVC-related state of the managed cluster. 
[**cluster_evc_manager_get_managed_cluster**](ClusterEVCManagerApi.md#cluster_evc_manager_get_managed_cluster) | **GET** /ClusterEVCManager/{moId}/managedCluster | Cluster associated with this manager object. 
[**cluster_evc_manager_get_value**](ClusterEVCManagerApi.md#cluster_evc_manager_get_value) | **GET** /ClusterEVCManager/{moId}/value | List of custom field values. 
[**cluster_evc_manager_set_custom_value**](ClusterEVCManagerApi.md#cluster_evc_manager_set_custom_value) | **POST** /ClusterEVCManager/{moId}/setCustomValue | Assigns a value to a custom field. 


# **cluster_evc_manager_check_add_host_evc_task**
> ManagedObjectReference cluster_evc_manager_check_add_host_evc_task(mo_id, check_add_host_evc_request_type)

Test the validity of adding a host into the managed cluster. 

Test the validity of adding a host into the managed cluster.  Note that this method only tests EVC admission control; host-add may fail for other reasons.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_add_host_evc_request_type import CheckAddHostEvcRequestType
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_add_host_evc_request_type = vmware_vi.CheckAddHostEvcRequestType() # CheckAddHostEvcRequestType | 

    try:
        # Test the validity of adding a host into the managed cluster. 
        api_response = api_instance.cluster_evc_manager_check_add_host_evc_task(mo_id, check_add_host_evc_request_type)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_check_add_host_evc_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_check_add_host_evc_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_add_host_evc_request_type** | [**CheckAddHostEvcRequestType**](CheckAddHostEvcRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidLogin***: if authentication with the host fails.  ***HostConnectFault***: if an error occurred when attempting to connect to the host. Typically, a more specific subclass is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_evc_manager_check_configure_evc_mode_task**
> ManagedObjectReference cluster_evc_manager_check_configure_evc_mode_task(mo_id, check_configure_evc_mode_request_type)

Test the validity of configuring an EVC mode on the managed cluster. 

Test the validity of configuring an EVC mode on the managed cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_configure_evc_mode_request_type import CheckConfigureEvcModeRequestType
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_configure_evc_mode_request_type = vmware_vi.CheckConfigureEvcModeRequestType() # CheckConfigureEvcModeRequestType | 

    try:
        # Test the validity of configuring an EVC mode on the managed cluster. 
        api_response = api_instance.cluster_evc_manager_check_configure_evc_mode_task(mo_id, check_configure_evc_mode_request_type)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_check_configure_evc_mode_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_check_configure_evc_mode_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_configure_evc_mode_request_type** | [**CheckConfigureEvcModeRequestType**](CheckConfigureEvcModeRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_evc_manager_configure_evc_mode_task**
> ManagedObjectReference cluster_evc_manager_configure_evc_mode_task(mo_id, configure_evc_mode_request_type)

Set the EVC mode. 

Set the EVC mode.  If EVC is currently disabled, then this will enable EVC. The parameter must specify a key to one of the EVC modes listed in the *ClusterEVCManagerEVCState.supportedEVCMode* array property. If there are no modes listed there, then EVC may not currently be enabled; reference the other properties in *ClusterEVCManagerEVCState* to determine what conditions are blocking EVC.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_evc_mode_request_type import ConfigureEvcModeRequestType
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_evc_mode_request_type = vmware_vi.ConfigureEvcModeRequestType() # ConfigureEvcModeRequestType | 

    try:
        # Set the EVC mode. 
        api_response = api_instance.cluster_evc_manager_configure_evc_mode_task(mo_id, configure_evc_mode_request_type)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_configure_evc_mode_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_configure_evc_mode_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_evc_mode_request_type** | [**ConfigureEvcModeRequestType**](ConfigureEvcModeRequestType.md)|  | 

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
**500** | ***EVCConfigFault***: if configuring EVC failed. Typically, a more specific subclass is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_evc_manager_disable_evc_mode_task**
> ManagedObjectReference cluster_evc_manager_disable_evc_mode_task(mo_id)

Disable EVC. 

Disable EVC.  EVC may be disabled at any time.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Inventory.EditCluster 

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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Disable EVC. 
        api_response = api_instance.cluster_evc_manager_disable_evc_mode_task(mo_id)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_disable_evc_mode_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_disable_evc_mode_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_evc_manager_get_available_field**
> List[CustomFieldDef] cluster_evc_manager_get_available_field(mo_id)

List of custom field definitions that are valid for the object's type. 

List of custom field definitions that are valid for the object's type.  The fields are sorted by *CustomFieldDef.name*.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_def import CustomFieldDef
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.cluster_evc_manager_get_available_field(mo_id)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_get_available_field: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldDef]**](CustomFieldDef.md)

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

# **cluster_evc_manager_get_evc_state**
> ClusterEVCManagerEVCState cluster_evc_manager_get_evc_state(mo_id)

EVC-related state of the managed cluster. 

EVC-related state of the managed cluster.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_evc_manager_evc_state import ClusterEVCManagerEVCState
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # EVC-related state of the managed cluster. 
        api_response = api_instance.cluster_evc_manager_get_evc_state(mo_id)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_get_evc_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_get_evc_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterEVCManagerEVCState**](ClusterEVCManagerEVCState.md)

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

# **cluster_evc_manager_get_managed_cluster**
> ManagedObjectReference cluster_evc_manager_get_managed_cluster(mo_id)

Cluster associated with this manager object. 

Cluster associated with this manager object.  ***Since:*** vSphere API 6.0 

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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Cluster associated with this manager object. 
        api_response = api_instance.cluster_evc_manager_get_managed_cluster(mo_id)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_get_managed_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_get_managed_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *ClusterComputeResource*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_evc_manager_get_value**
> List[CustomFieldValue] cluster_evc_manager_get_value(mo_id)

List of custom field values. 

List of custom field values.  Each value uses a key to associate an instance of a *CustomFieldStringValue* with a custom field definition.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_value import CustomFieldValue
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.cluster_evc_manager_get_value(mo_id)
        print("The response of ClusterEVCManagerApi->cluster_evc_manager_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_get_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldValue]**](CustomFieldValue.md)

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

# **cluster_evc_manager_set_custom_value**
> cluster_evc_manager_set_custom_value(mo_id, set_custom_value_request_type)

Assigns a value to a custom field. 

Assigns a value to a custom field.  The setCustomValue method requires whichever updatePrivilege is defined as one of the *CustomFieldDef.fieldInstancePrivileges* for the CustomFieldDef whose value is being changed.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_custom_value_request_type import SetCustomValueRequestType
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
    api_instance = vmware_vi.ClusterEVCManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.cluster_evc_manager_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling ClusterEVCManagerApi->cluster_evc_manager_set_custom_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_custom_value_request_type** | [**SetCustomValueRequestType**](SetCustomValueRequestType.md)|  | 

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

