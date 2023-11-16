# vmware_vi.FailoverClusterConfiguratorApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**failover_cluster_configurator_configure_vcha_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_configure_vcha_task) | **POST** /FailoverClusterConfigurator/{moId}/configureVcha_Task | Configure VCHA on the local vCenter Server. 
[**failover_cluster_configurator_create_passive_node_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_create_passive_node_task) | **POST** /FailoverClusterConfigurator/{moId}/createPassiveNode_Task | Creates a Passive node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 
[**failover_cluster_configurator_create_witness_node_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_create_witness_node_task) | **POST** /FailoverClusterConfigurator/{moId}/createWitnessNode_Task | Creates a Witness node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 
[**failover_cluster_configurator_deploy_vcha_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_deploy_vcha_task) | **POST** /FailoverClusterConfigurator/{moId}/deployVcha_Task | Deploys and Configures VCHA on the local vCenter as a single API. 
[**failover_cluster_configurator_destroy_vcha_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_destroy_vcha_task) | **POST** /FailoverClusterConfigurator/{moId}/destroyVcha_Task | Destroys the VCHA cluster setup and removes all VCHA specific configuration from the VCVA appliance. 
[**failover_cluster_configurator_get_disabled_configure_method**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_get_disabled_configure_method) | **GET** /FailoverClusterConfigurator/{moId}/disabledConfigureMethod | A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 
[**failover_cluster_configurator_get_vcha_config**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_get_vcha_config) | **POST** /FailoverClusterConfigurator/{moId}/getVchaConfig | Returns the configuration information for each node that is part of the VCHA Cluster. 
[**failover_cluster_configurator_prepare_vcha_task**](FailoverClusterConfiguratorApi.md#failover_cluster_configurator_prepare_vcha_task) | **POST** /FailoverClusterConfigurator/{moId}/prepareVcha_Task | Prepares the vCenter appliance for a VCHA cluster deployment. 


# **failover_cluster_configurator_configure_vcha_task**
> ManagedObjectReference failover_cluster_configurator_configure_vcha_task(mo_id, configure_vcha_request_type)

Configure VCHA on the local vCenter Server. 

Configure VCHA on the local vCenter Server.  This operation configures the VC appliance with VCHA specific inputs and uses already deployed Passive and Witness nodes to set up the VCHA cluster. After configuration, the VCHA Cluster is enabled on a best effort basis, but if this operation does not succeed, *FailoverClusterManager.setClusterMode_Task* must be called to enable it. State replication or failover is not allowed until the VCHA Cluster is enabled. The current vCenter Server continues to serve client requests during and after the configuration.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_vcha_request_type import ConfigureVchaRequestType
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_vcha_request_type = vmware_vi.ConfigureVchaRequestType() # ConfigureVchaRequestType | 

    try:
        # Configure VCHA on the local vCenter Server. 
        api_response = api_instance.failover_cluster_configurator_configure_vcha_task(mo_id, configure_vcha_request_type)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_configure_vcha_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_configure_vcha_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_vcha_request_type** | [**ConfigureVchaRequestType**](ConfigureVchaRequestType.md)|  | 

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

# **failover_cluster_configurator_create_passive_node_task**
> ManagedObjectReference failover_cluster_configurator_create_passive_node_task(mo_id, create_passive_node_request_type)

Creates a Passive node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 

Creates a Passive node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_passive_node_request_type import CreatePassiveNodeRequestType
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_passive_node_request_type = vmware_vi.CreatePassiveNodeRequestType() # CreatePassiveNodeRequestType | 

    try:
        # Creates a Passive node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 
        api_response = api_instance.failover_cluster_configurator_create_passive_node_task(mo_id, create_passive_node_request_type)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_create_passive_node_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_create_passive_node_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_passive_node_request_type** | [**CreatePassiveNodeRequestType**](CreatePassiveNodeRequestType.md)|  | 

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

# **failover_cluster_configurator_create_witness_node_task**
> ManagedObjectReference failover_cluster_configurator_create_witness_node_task(mo_id, create_witness_node_request_type)

Creates a Witness node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 

Creates a Witness node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_witness_node_request_type import CreateWitnessNodeRequestType
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_witness_node_request_type = vmware_vi.CreateWitnessNodeRequestType() # CreateWitnessNodeRequestType | 

    try:
        # Creates a Witness node in a degraded VCHA Cluster with node location information and pre-existing VCHA Cluster configuration from the Active node. 
        api_response = api_instance.failover_cluster_configurator_create_witness_node_task(mo_id, create_witness_node_request_type)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_create_witness_node_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_create_witness_node_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_witness_node_request_type** | [**CreateWitnessNodeRequestType**](CreateWitnessNodeRequestType.md)|  | 

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

# **failover_cluster_configurator_deploy_vcha_task**
> ManagedObjectReference failover_cluster_configurator_deploy_vcha_task(mo_id, deploy_vcha_request_type)

Deploys and Configures VCHA on the local vCenter as a single API. 

Deploys and Configures VCHA on the local vCenter as a single API.  This deployment operation automatically provisions and creates a Passive and a Witness node followed by configuring each node such that a 3 node VCHA Cluster is formed. After configuration, the VCHA Cluster is enabled on a best effort basis, but if this operation does not succeed, *FailoverClusterManager.setClusterMode_Task* must be called to enable it. State replication or failover is not allowed until the VCHA Cluster is enabled. The current vCenter Server continues to serve client requests during and after the deployment. If the activeVcNetworkConfig spec if filled in, the cluster network will be created and configured. No changes will be made if the cluster network is already configured.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.deploy_vcha_request_type import DeployVchaRequestType
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    deploy_vcha_request_type = vmware_vi.DeployVchaRequestType() # DeployVchaRequestType | 

    try:
        # Deploys and Configures VCHA on the local vCenter as a single API. 
        api_response = api_instance.failover_cluster_configurator_deploy_vcha_task(mo_id, deploy_vcha_request_type)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_deploy_vcha_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_deploy_vcha_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **deploy_vcha_request_type** | [**DeployVchaRequestType**](DeployVchaRequestType.md)|  | 

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

# **failover_cluster_configurator_destroy_vcha_task**
> ManagedObjectReference failover_cluster_configurator_destroy_vcha_task(mo_id)

Destroys the VCHA cluster setup and removes all VCHA specific configuration from the VCVA appliance. 

Destroys the VCHA cluster setup and removes all VCHA specific configuration from the VCVA appliance.  The active node in the cluster continues to run as a standalone VCVA appliance after the destroy operation has been performed. This operation is allowed under the following circumstances: \\- VCHA cluster is disabled \\- The node is in an isolated state \\- VCHA Deploy/Configure has failed  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys the VCHA cluster setup and removes all VCHA specific configuration from the VCVA appliance. 
        api_response = api_instance.failover_cluster_configurator_destroy_vcha_task(mo_id)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_destroy_vcha_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_destroy_vcha_task: %s\n" % e)
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

# **failover_cluster_configurator_get_disabled_configure_method**
> List[str] failover_cluster_configurator_get_disabled_configure_method(mo_id)

A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 

A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for.  This list may include the following methods: - *FailoverClusterConfigurator.deployVcha_Task* - *FailoverClusterConfigurator.configureVcha_Task* - *FailoverClusterConfigurator.createPassiveNode_Task* - *FailoverClusterConfigurator.createWitnessNode_Task* - *FailoverClusterConfigurator.destroyVcha_Task*    As with other disabled methods there will be no property updates on this property when called with non-zero property collector versions.  ***Since:*** vSphere API 6.5 

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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of method names that must not be called and will throw a fault due to some other method running that the disabled method can cause side-effects for. 
        api_response = api_instance.failover_cluster_configurator_get_disabled_configure_method(mo_id)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_get_disabled_configure_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_get_disabled_configure_method: %s\n" % e)
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

# **failover_cluster_configurator_get_vcha_config**
> VchaClusterConfigInfo failover_cluster_configurator_get_vcha_config(mo_id)

Returns the configuration information for each node that is part of the VCHA Cluster. 

Returns the configuration information for each node that is part of the VCHA Cluster.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.vcha_cluster_config_info import VchaClusterConfigInfo
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns the configuration information for each node that is part of the VCHA Cluster. 
        api_response = api_instance.failover_cluster_configurator_get_vcha_config(mo_id)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_get_vcha_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_get_vcha_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VchaClusterConfigInfo**](VchaClusterConfigInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a data structure specifying configuration for Active, Passive and Witness node in the Cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failover_cluster_configurator_prepare_vcha_task**
> ManagedObjectReference failover_cluster_configurator_prepare_vcha_task(mo_id, prepare_vcha_request_type)

Prepares the vCenter appliance for a VCHA cluster deployment. 

Prepares the vCenter appliance for a VCHA cluster deployment.  This preparation operation saves the network configuration of the cluster and configures the Active node to be cloned for a VCHA configuration. Prepares the VCHA Active node for ssh keys, vpostgres replication and related configuration file setup needed for a VCHA cluster. If the Active node Cluster network adapter does not exist the prepare operation will fail. No changes will be made if the cluster is already configured.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Global.VCServer 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.prepare_vcha_request_type import PrepareVchaRequestType
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
    api_instance = vmware_vi.FailoverClusterConfiguratorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    prepare_vcha_request_type = vmware_vi.PrepareVchaRequestType() # PrepareVchaRequestType | 

    try:
        # Prepares the vCenter appliance for a VCHA cluster deployment. 
        api_response = api_instance.failover_cluster_configurator_prepare_vcha_task(mo_id, prepare_vcha_request_type)
        print("The response of FailoverClusterConfiguratorApi->failover_cluster_configurator_prepare_vcha_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverClusterConfiguratorApi->failover_cluster_configurator_prepare_vcha_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **prepare_vcha_request_type** | [**PrepareVchaRequestType**](PrepareVchaRequestType.md)|  | 

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

