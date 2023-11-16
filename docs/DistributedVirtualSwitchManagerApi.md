# vmware_vi.DistributedVirtualSwitchManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributed_virtual_switch_manager_dvs_manager_export_entity_task**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_dvs_manager_export_entity_task) | **POST** /DistributedVirtualSwitchManager/{moId}/DVSManagerExportEntity_Task | Export the configuration for entities specified in the &lt;code&gt;selectionSet&lt;/code&gt; parameter. 
[**distributed_virtual_switch_manager_dvs_manager_import_entity_task**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_dvs_manager_import_entity_task) | **POST** /DistributedVirtualSwitchManager/{moId}/DVSManagerImportEntity_Task | Import the configuration of entities specified in *EntityBackupConfig*. 
[**distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group) | **POST** /DistributedVirtualSwitchManager/{moId}/DVSManagerLookupDvPortGroup | Returns the portgroup identified by the key within the specified VDS identified by its UUID. 
[**distributed_virtual_switch_manager_query_available_dvs_spec**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_available_dvs_spec) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryAvailableDvsSpec | This operation returns a list of switch product specifications that are supported by the vCenter Server. 
[**distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryCompatibleHostForExistingDvs | This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_query_compatible_host_for_new_dvs**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_compatible_host_for_new_dvs) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryCompatibleHostForNewDvs | This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryCompatibleVmnicsFromHosts | This operation returns a list of vmnics which are compatible with the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_query_dvs_by_uuid**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_dvs_by_uuid) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryDvsByUuid | This operation returns a DistributedVirtualSwitch given a UUID. 
[**distributed_virtual_switch_manager_query_dvs_check_compatibility**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_dvs_check_compatibility) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryDvsCheckCompatibility | This operation returns a list of compatibility results. 
[**distributed_virtual_switch_manager_query_dvs_compatible_host_spec**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_dvs_compatible_host_spec) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryDvsCompatibleHostSpec | This operation returns a list of host product specifications that are compatible with the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_query_dvs_config_target**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_dvs_config_target) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryDvsConfigTarget | This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup configuration target on a host. 
[**distributed_virtual_switch_manager_query_dvs_feature_capability**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_dvs_feature_capability) | **POST** /DistributedVirtualSwitchManager/{moId}/QueryDvsFeatureCapability | This operation indicates which version-specific DVS features are available for the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_query_supported_network_offload_spec**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_query_supported_network_offload_spec) | **POST** /DistributedVirtualSwitchManager/{moId}/QuerySupportedNetworkOffloadSpec | This operation returns a list of network offload specifications that are compatible with the given DistributedVirtualSwitch product specification. 
[**distributed_virtual_switch_manager_rectify_dvs_on_host_task**](DistributedVirtualSwitchManagerApi.md#distributed_virtual_switch_manager_rectify_dvs_on_host_task) | **POST** /DistributedVirtualSwitchManager/{moId}/RectifyDvsOnHost_Task | Update the Distributed Switch configuration on the hosts to bring them in sync with the current configuration in vCenter Server. 


# **distributed_virtual_switch_manager_dvs_manager_export_entity_task**
> ManagedObjectReference distributed_virtual_switch_manager_dvs_manager_export_entity_task(mo_id, dvs_manager_export_entity_request_type)

Export the configuration for entities specified in the <code>selectionSet</code> parameter. 

Export the configuration for entities specified in the <code>selectionSet</code> parameter.  You can use this method only for a *VmwareDistributedVirtualSwitch* and its associated *DistributedVirtualPortgroup* objects.  Use the *DistributedVirtualSwitchManager.DVSManagerImportEntity_Task* method to restore the entity to the state represented by the exported configuration. You can also use the exported configuration to create a new switch or portgroup.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_manager_export_entity_request_type import DVSManagerExportEntityRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dvs_manager_export_entity_request_type = vmware_vi.DVSManagerExportEntityRequestType() # DVSManagerExportEntityRequestType | 

    try:
        # Export the configuration for entities specified in the <code>selectionSet</code> parameter. 
        api_response = api_instance.distributed_virtual_switch_manager_dvs_manager_export_entity_task(mo_id, dvs_manager_export_entity_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_export_entity_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_export_entity_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dvs_manager_export_entity_request_type** | [**DVSManagerExportEntityRequestType**](DVSManagerExportEntityRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. After successful completion, the *Task*.*Task.info*.*TaskInfo.result* property contains the *EntityBackupConfig* object.  Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: If entity in selectionSet doesn&#39;t exist.  ***BackupBlobWriteFailure***: if failed to create backup config blob.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_dvs_manager_import_entity_task**
> ManagedObjectReference distributed_virtual_switch_manager_dvs_manager_import_entity_task(mo_id, dvs_manager_import_entity_request_type)

Import the configuration of entities specified in *EntityBackupConfig*. 

Import the configuration of entities specified in *EntityBackupConfig*.  You can restore the existing configuration to the state represented by the backup configuration. You can also use the backup configuration to create a new switch or portgroup. See *EntityImportType_enum*.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_manager_import_entity_request_type import DVSManagerImportEntityRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dvs_manager_import_entity_request_type = vmware_vi.DVSManagerImportEntityRequestType() # DVSManagerImportEntityRequestType | 

    try:
        # Import the configuration of entities specified in *EntityBackupConfig*. 
        api_response = api_instance.distributed_virtual_switch_manager_dvs_manager_import_entity_task(mo_id, dvs_manager_import_entity_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_import_entity_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_import_entity_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dvs_manager_import_entity_request_type** | [**DVSManagerImportEntityRequestType**](DVSManagerImportEntityRequestType.md)|  | 

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
**500** | ***NotFound***: If entity in *EntityBackupConfig.key* doesn&#39;t exist.  ***DvsFault***: if operation fails on any host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group**
> ManagedObjectReference distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group(mo_id, dvs_manager_lookup_dv_port_group_request_type)

Returns the portgroup identified by the key within the specified VDS identified by its UUID. 

Returns the portgroup identified by the key within the specified VDS identified by its UUID.  ***Since:*** vSphere API 5.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_manager_lookup_dv_port_group_request_type import DVSManagerLookupDvPortGroupRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dvs_manager_lookup_dv_port_group_request_type = vmware_vi.DVSManagerLookupDvPortGroupRequestType() # DVSManagerLookupDvPortGroupRequestType | 

    try:
        # Returns the portgroup identified by the key within the specified VDS identified by its UUID. 
        api_response = api_instance.distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group(mo_id, dvs_manager_lookup_dv_port_group_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_dvs_manager_lookup_dv_port_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dvs_manager_lookup_dv_port_group_request_type** | [**DVSManagerLookupDvPortGroupRequestType**](DVSManagerLookupDvPortGroupRequestType.md)|  | 

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
**200** | Refers instance of *DistributedVirtualPortgroup*.  |  -  |
**500** | ***NotFound***: If the portgroup for the specified inputs was not found.  ***NotSupported***: If the operation is not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_query_available_dvs_spec**
> List[DistributedVirtualSwitchProductSpec] distributed_virtual_switch_manager_query_available_dvs_spec(mo_id, query_available_dvs_spec_request_type)

This operation returns a list of switch product specifications that are supported by the vCenter Server. 

This operation returns a list of switch product specifications that are supported by the vCenter Server.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.distributed_virtual_switch_product_spec import DistributedVirtualSwitchProductSpec
from vmware_vi.models.query_available_dvs_spec_request_type import QueryAvailableDvsSpecRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_available_dvs_spec_request_type = vmware_vi.QueryAvailableDvsSpecRequestType() # QueryAvailableDvsSpecRequestType | 

    try:
        # This operation returns a list of switch product specifications that are supported by the vCenter Server. 
        api_response = api_instance.distributed_virtual_switch_manager_query_available_dvs_spec(mo_id, query_available_dvs_spec_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_available_dvs_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_available_dvs_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_available_dvs_spec_request_type** | [**QueryAvailableDvsSpecRequestType**](QueryAvailableDvsSpecRequestType.md)|  | 

### Return type

[**List[DistributedVirtualSwitchProductSpec]**](DistributedVirtualSwitchProductSpec.md)

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

# **distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs**
> List[ManagedObjectReference] distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs(mo_id, query_compatible_host_for_existing_dvs_request_type)

This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 

This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_compatible_host_for_existing_dvs_request_type import QueryCompatibleHostForExistingDvsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_compatible_host_for_existing_dvs_request_type = vmware_vi.QueryCompatibleHostForExistingDvsRequestType() # QueryCompatibleHostForExistingDvsRequestType | 

    try:
        # This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs(mo_id, query_compatible_host_for_existing_dvs_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_host_for_existing_dvs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_compatible_host_for_existing_dvs_request_type** | [**QueryCompatibleHostForExistingDvsRequestType**](QueryCompatibleHostForExistingDvsRequestType.md)|  | 

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
**200** | Refers instances of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_query_compatible_host_for_new_dvs**
> List[ManagedObjectReference] distributed_virtual_switch_manager_query_compatible_host_for_new_dvs(mo_id, query_compatible_host_for_new_dvs_request_type)

This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 

This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_compatible_host_for_new_dvs_request_type import QueryCompatibleHostForNewDvsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_compatible_host_for_new_dvs_request_type = vmware_vi.QueryCompatibleHostForNewDvsRequestType() # QueryCompatibleHostForNewDvsRequestType | 

    try:
        # This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_compatible_host_for_new_dvs(mo_id, query_compatible_host_for_new_dvs_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_host_for_new_dvs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_host_for_new_dvs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_compatible_host_for_new_dvs_request_type** | [**QueryCompatibleHostForNewDvsRequestType**](QueryCompatibleHostForNewDvsRequestType.md)|  | 

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
**200** | Refers instances of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts**
> List[DVSManagerPhysicalNicsList] distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts(mo_id, query_compatible_vmnics_from_hosts_request_type)

This operation returns a list of vmnics which are compatible with the given DistributedVirtualSwitch product specification. 

This operation returns a list of vmnics which are compatible with the given DistributedVirtualSwitch product specification.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_manager_physical_nics_list import DVSManagerPhysicalNicsList
from vmware_vi.models.query_compatible_vmnics_from_hosts_request_type import QueryCompatibleVmnicsFromHostsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_compatible_vmnics_from_hosts_request_type = vmware_vi.QueryCompatibleVmnicsFromHostsRequestType() # QueryCompatibleVmnicsFromHostsRequestType | 

    try:
        # This operation returns a list of vmnics which are compatible with the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts(mo_id, query_compatible_vmnics_from_hosts_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_compatible_vmnics_from_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_compatible_vmnics_from_hosts_request_type** | [**QueryCompatibleVmnicsFromHostsRequestType**](QueryCompatibleVmnicsFromHostsRequestType.md)|  | 

### Return type

[**List[DVSManagerPhysicalNicsList]**](DVSManagerPhysicalNicsList.md)

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

# **distributed_virtual_switch_manager_query_dvs_by_uuid**
> ManagedObjectReference distributed_virtual_switch_manager_query_dvs_by_uuid(mo_id, query_dvs_by_uuid_request_type)

This operation returns a DistributedVirtualSwitch given a UUID. 

This operation returns a DistributedVirtualSwitch given a UUID.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_dvs_by_uuid_request_type import QueryDvsByUuidRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_dvs_by_uuid_request_type = vmware_vi.QueryDvsByUuidRequestType() # QueryDvsByUuidRequestType | 

    try:
        # This operation returns a DistributedVirtualSwitch given a UUID. 
        api_response = api_instance.distributed_virtual_switch_manager_query_dvs_by_uuid(mo_id, query_dvs_by_uuid_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_by_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_dvs_by_uuid_request_type** | [**QueryDvsByUuidRequestType**](QueryDvsByUuidRequestType.md)|  | 

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
**200** | Refers instance of *DistributedVirtualSwitch*.  |  -  |
**500** | ***NotFound***: If a switch with the UUID doesn&#39;t exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_manager_query_dvs_check_compatibility**
> List[DistributedVirtualSwitchManagerCompatibilityResult] distributed_virtual_switch_manager_query_dvs_check_compatibility(mo_id, query_dvs_check_compatibility_request_type)

This operation returns a list of compatibility results. 

This operation returns a list of compatibility results.  Each compatibility result is an object that has a host property and optionally a fault which would be populated only if that host is not compatible with a given dvsProductSpec. All filters in hostFilerSpecs are ANDed to derive the intersection of hosts against which compatibility is checked. If caller did not have view privileges on the host entity in an element of the CompatibilityResult array, then that entire element would be removed from the CompatibilityResult array. Typical uses: - For the createDVS situation, hostFilterSpec is of type HostDvsFilterSpec and DvsProductSpec   will have newSwitchProductSpec set. - For the Add-Host-To-DVS situation, you can use either HostDvsFilterSpec or   HostDvsMembershipFilter with inclusive being false, and pass the DVS in DvsProductSpec. - For the Upgrade-DVS situation, you can use either HostDvsFilterSpec or   HostDvsMembershipFilter with inclusive being true, and pass the new desired ProductSpec   for DVS in newSwitchProductSpec.    ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.distributed_virtual_switch_manager_compatibility_result import DistributedVirtualSwitchManagerCompatibilityResult
from vmware_vi.models.query_dvs_check_compatibility_request_type import QueryDvsCheckCompatibilityRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_dvs_check_compatibility_request_type = vmware_vi.QueryDvsCheckCompatibilityRequestType() # QueryDvsCheckCompatibilityRequestType | 

    try:
        # This operation returns a list of compatibility results. 
        api_response = api_instance.distributed_virtual_switch_manager_query_dvs_check_compatibility(mo_id, query_dvs_check_compatibility_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_check_compatibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_check_compatibility: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_dvs_check_compatibility_request_type** | [**QueryDvsCheckCompatibilityRequestType**](QueryDvsCheckCompatibilityRequestType.md)|  | 

### Return type

[**List[DistributedVirtualSwitchManagerCompatibilityResult]**](DistributedVirtualSwitchManagerCompatibilityResult.md)

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

# **distributed_virtual_switch_manager_query_dvs_compatible_host_spec**
> List[DistributedVirtualSwitchHostProductSpec] distributed_virtual_switch_manager_query_dvs_compatible_host_spec(mo_id, query_dvs_compatible_host_spec_request_type)

This operation returns a list of host product specifications that are compatible with the given DistributedVirtualSwitch product specification. 

This operation returns a list of host product specifications that are compatible with the given DistributedVirtualSwitch product specification.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.distributed_virtual_switch_host_product_spec import DistributedVirtualSwitchHostProductSpec
from vmware_vi.models.query_dvs_compatible_host_spec_request_type import QueryDvsCompatibleHostSpecRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_dvs_compatible_host_spec_request_type = vmware_vi.QueryDvsCompatibleHostSpecRequestType() # QueryDvsCompatibleHostSpecRequestType | 

    try:
        # This operation returns a list of host product specifications that are compatible with the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_dvs_compatible_host_spec(mo_id, query_dvs_compatible_host_spec_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_compatible_host_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_compatible_host_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_dvs_compatible_host_spec_request_type** | [**QueryDvsCompatibleHostSpecRequestType**](QueryDvsCompatibleHostSpecRequestType.md)|  | 

### Return type

[**List[DistributedVirtualSwitchHostProductSpec]**](DistributedVirtualSwitchHostProductSpec.md)

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

# **distributed_virtual_switch_manager_query_dvs_config_target**
> DVSManagerDvsConfigTarget distributed_virtual_switch_manager_query_dvs_config_target(mo_id, query_dvs_config_target_request_type)

This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup configuration target on a host. 

This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup configuration target on a host.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_manager_dvs_config_target import DVSManagerDvsConfigTarget
from vmware_vi.models.query_dvs_config_target_request_type import QueryDvsConfigTargetRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_dvs_config_target_request_type = vmware_vi.QueryDvsConfigTargetRequestType() # QueryDvsConfigTargetRequestType | 

    try:
        # This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup configuration target on a host. 
        api_response = api_instance.distributed_virtual_switch_manager_query_dvs_config_target(mo_id, query_dvs_config_target_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_config_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_config_target: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_dvs_config_target_request_type** | [**QueryDvsConfigTargetRequestType**](QueryDvsConfigTargetRequestType.md)|  | 

### Return type

[**DVSManagerDvsConfigTarget**](DVSManagerDvsConfigTarget.md)

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

# **distributed_virtual_switch_manager_query_dvs_feature_capability**
> DVSFeatureCapability distributed_virtual_switch_manager_query_dvs_feature_capability(mo_id, query_dvs_feature_capability_request_type)

This operation indicates which version-specific DVS features are available for the given DistributedVirtualSwitch product specification. 

This operation indicates which version-specific DVS features are available for the given DistributedVirtualSwitch product specification.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_feature_capability import DVSFeatureCapability
from vmware_vi.models.query_dvs_feature_capability_request_type import QueryDvsFeatureCapabilityRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_dvs_feature_capability_request_type = vmware_vi.QueryDvsFeatureCapabilityRequestType() # QueryDvsFeatureCapabilityRequestType | 

    try:
        # This operation indicates which version-specific DVS features are available for the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_dvs_feature_capability(mo_id, query_dvs_feature_capability_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_feature_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_dvs_feature_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_dvs_feature_capability_request_type** | [**QueryDvsFeatureCapabilityRequestType**](QueryDvsFeatureCapabilityRequestType.md)|  | 

### Return type

[**DVSFeatureCapability**](DVSFeatureCapability.md)

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

# **distributed_virtual_switch_manager_query_supported_network_offload_spec**
> List[DistributedVirtualSwitchNetworkOffloadSpec] distributed_virtual_switch_manager_query_supported_network_offload_spec(mo_id, query_supported_network_offload_spec_request_type)

This operation returns a list of network offload specifications that are compatible with the given DistributedVirtualSwitch product specification. 

This operation returns a list of network offload specifications that are compatible with the given DistributedVirtualSwitch product specification.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.distributed_virtual_switch_network_offload_spec import DistributedVirtualSwitchNetworkOffloadSpec
from vmware_vi.models.query_supported_network_offload_spec_request_type import QuerySupportedNetworkOffloadSpecRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_supported_network_offload_spec_request_type = vmware_vi.QuerySupportedNetworkOffloadSpecRequestType() # QuerySupportedNetworkOffloadSpecRequestType | 

    try:
        # This operation returns a list of network offload specifications that are compatible with the given DistributedVirtualSwitch product specification. 
        api_response = api_instance.distributed_virtual_switch_manager_query_supported_network_offload_spec(mo_id, query_supported_network_offload_spec_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_supported_network_offload_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_query_supported_network_offload_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_supported_network_offload_spec_request_type** | [**QuerySupportedNetworkOffloadSpecRequestType**](QuerySupportedNetworkOffloadSpecRequestType.md)|  | 

### Return type

[**List[DistributedVirtualSwitchNetworkOffloadSpec]**](DistributedVirtualSwitchNetworkOffloadSpec.md)

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

# **distributed_virtual_switch_manager_rectify_dvs_on_host_task**
> ManagedObjectReference distributed_virtual_switch_manager_rectify_dvs_on_host_task(mo_id, rectify_dvs_on_host_request_type)

Update the Distributed Switch configuration on the hosts to bring them in sync with the current configuration in vCenter Server. 

Update the Distributed Switch configuration on the hosts to bring them in sync with the current configuration in vCenter Server.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.rectify_dvs_on_host_request_type import RectifyDvsOnHostRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rectify_dvs_on_host_request_type = vmware_vi.RectifyDvsOnHostRequestType() # RectifyDvsOnHostRequestType | 

    try:
        # Update the Distributed Switch configuration on the hosts to bring them in sync with the current configuration in vCenter Server. 
        api_response = api_instance.distributed_virtual_switch_manager_rectify_dvs_on_host_task(mo_id, rectify_dvs_on_host_request_type)
        print("The response of DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_rectify_dvs_on_host_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchManagerApi->distributed_virtual_switch_manager_rectify_dvs_on_host_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rectify_dvs_on_host_request_type** | [**RectifyDvsOnHostRequestType**](RectifyDvsOnHostRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

