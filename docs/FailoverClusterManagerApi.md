# vmware_vi.FailoverClusterManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**failover_cluster_manager_get_cluster_mode**](FailoverClusterManagerApi.md#failover_cluster_manager_get_cluster_mode) | **POST** /FailoverClusterManager/{moId}/getClusterMode | Returns current mode of a VCHA Cluster. 
[**failover_cluster_manager_get_disabled_cluster_method**](FailoverClusterManagerApi.md#failover_cluster_manager_get_disabled_cluster_method) | **GET** /FailoverClusterManager/{moId}/disabledClusterMethod | A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 
[**failover_cluster_manager_get_vcha_cluster_health**](FailoverClusterManagerApi.md#failover_cluster_manager_get_vcha_cluster_health) | **POST** /FailoverClusterManager/{moId}/GetVchaClusterHealth | Returns last known health of the VCHA Cluster. 
[**failover_cluster_manager_initiate_failover_task**](FailoverClusterManagerApi.md#failover_cluster_manager_initiate_failover_task) | **POST** /FailoverClusterManager/{moId}/initiateFailover_Task | Allows a caller to initiate a failover from Active vCenter Server node to the Passive node. 
[**failover_cluster_manager_set_cluster_mode_task**](FailoverClusterManagerApi.md#failover_cluster_manager_set_cluster_mode_task) | **POST** /FailoverClusterManager/{moId}/setClusterMode_Task | setClusterMode method allows caller to manipulate the mode of a VCHA Cluster Following mode transitions are allowed - enabled -&amp;gt; disabled - Allowed only in healthy and degraded states. 


# **failover_cluster_manager_get_cluster_mode**
> str failover_cluster_manager_get_cluster_mode(mo_id)

Returns current mode of a VCHA Cluster. 

Returns current mode of a VCHA Cluster.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.FailoverClusterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns current mode of a VCHA Cluster. 
        api_response = api_instance.failover_cluster_manager_get_cluster_mode(mo_id)
        print("The response of FailoverClusterManagerApi->failover_cluster_manager_get_cluster_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterManagerApi->failover_cluster_manager_get_cluster_mode: %s\n" % e)
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

# **failover_cluster_manager_get_disabled_cluster_method**
> List[str] failover_cluster_manager_get_disabled_cluster_method(mo_id)

A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 

A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for.  This list may include the following methods: - *FailoverClusterManager.setClusterMode_Task* - *FailoverClusterManager.getClusterMode* - *FailoverClusterManager.initiateFailover_Task* - *FailoverClusterManager.GetVchaClusterHealth*    GetClusterHealth will also be disabled if Deploy is in progress. As with other disabled methods there will be no property updates on this property when called with non-zero property collector versions.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.FailoverClusterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 
        api_response = api_instance.failover_cluster_manager_get_disabled_cluster_method(mo_id)
        print("The response of FailoverClusterManagerApi->failover_cluster_manager_get_disabled_cluster_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterManagerApi->failover_cluster_manager_get_disabled_cluster_method: %s\n" % e)
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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failover_cluster_manager_get_vcha_cluster_health**
> VchaClusterHealth failover_cluster_manager_get_vcha_cluster_health(mo_id)

Returns last known health of the VCHA Cluster. 

Returns last known health of the VCHA Cluster.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.vcha_cluster_health import VchaClusterHealth
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
    api_instance = vmware_vi.FailoverClusterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns last known health of the VCHA Cluster. 
        api_response = api_instance.failover_cluster_manager_get_vcha_cluster_health(mo_id)
        print("The response of FailoverClusterManagerApi->failover_cluster_manager_get_vcha_cluster_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterManagerApi->failover_cluster_manager_get_vcha_cluster_health: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VchaClusterHealth**](VchaClusterHealth.md)

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

# **failover_cluster_manager_initiate_failover_task**
> ManagedObjectReference failover_cluster_manager_initiate_failover_task(mo_id, initiate_failover_request_type)

Allows a caller to initiate a failover from Active vCenter Server node to the Passive node. 

Allows a caller to initiate a failover from Active vCenter Server node to the Passive node.  By default it is a forced failover. The planned flag can be used to initiate it as a planned failover. For forced failover, Active node immediately initiates a failover. This may result into a data loss after failover. For planned failover, Active node flushes all the state to the Passive node, waits for the flush to complete before causing a failover. After the failover, Passive node starts without any data loss. A failover is allowed only in the following cases - 1\\. Cluster's mode is enabled and all cluster members are present. 2\\. Cluster's mode is maintenance and all cluster members are present. API throws an exception in all other cases.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.initiate_failover_request_type import InitiateFailoverRequestType
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
    api_instance = vmware_vi.FailoverClusterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    initiate_failover_request_type = vmware_vi.InitiateFailoverRequestType() # InitiateFailoverRequestType | 

    try:
        # Allows a caller to initiate a failover from Active vCenter Server node to the Passive node. 
        api_response = api_instance.failover_cluster_manager_initiate_failover_task(mo_id, initiate_failover_request_type)
        print("The response of FailoverClusterManagerApi->failover_cluster_manager_initiate_failover_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterManagerApi->failover_cluster_manager_initiate_failover_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **initiate_failover_request_type** | [**InitiateFailoverRequestType**](InitiateFailoverRequestType.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failover_cluster_manager_set_cluster_mode_task**
> ManagedObjectReference failover_cluster_manager_set_cluster_mode_task(mo_id, set_cluster_mode_request_type)

setClusterMode method allows caller to manipulate the mode of a VCHA Cluster Following mode transitions are allowed - enabled -&gt; disabled - Allowed only in healthy and degraded states. 

setClusterMode method allows caller to manipulate the mode of a VCHA Cluster Following mode transitions are allowed - enabled -&gt; disabled - Allowed only in healthy and degraded states.  enabled -&gt; maintenance - Allowed only in healthy state. disabled -&gt; enabled - Allowed only in healthy state. maintenance -&gt; enabled - Allowed only in healthy state with all nodes are running the same version. maintenance -&gt; disabled - Allowed only in healthy state with all nodes are running the same version. All other transitions are not allowed. VCHA Cluster configuration remains intact in any of the cluster modes.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.set_cluster_mode_request_type import SetClusterModeRequestType
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
    api_instance = vmware_vi.FailoverClusterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_cluster_mode_request_type = vmware_vi.SetClusterModeRequestType() # SetClusterModeRequestType | 

    try:
        # setClusterMode method allows caller to manipulate the mode of a VCHA Cluster Following mode transitions are allowed - enabled -&gt; disabled - Allowed only in healthy and degraded states. 
        api_response = api_instance.failover_cluster_manager_set_cluster_mode_task(mo_id, set_cluster_mode_request_type)
        print("The response of FailoverClusterManagerApi->failover_cluster_manager_set_cluster_mode_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterManagerApi->failover_cluster_manager_set_cluster_mode_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_cluster_mode_request_type** | [**SetClusterModeRequestType**](SetClusterModeRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the progress of the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

