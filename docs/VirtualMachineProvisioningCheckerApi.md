# vmware_vi.VirtualMachineProvisioningCheckerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_provisioning_checker_check_clone_task**](VirtualMachineProvisioningCheckerApi.md#virtual_machine_provisioning_checker_check_clone_task) | **POST** /VirtualMachineProvisioningChecker/{moId}/CheckClone_Task | Tests the feasibility of a proposed *VirtualMachine.CloneVM_Task* operation. 
[**virtual_machine_provisioning_checker_check_instant_clone_task**](VirtualMachineProvisioningCheckerApi.md#virtual_machine_provisioning_checker_check_instant_clone_task) | **POST** /VirtualMachineProvisioningChecker/{moId}/CheckInstantClone_Task | Tests the feasibility of a proposed *VirtualMachine.InstantClone_Task* operation. 
[**virtual_machine_provisioning_checker_check_migrate_task**](VirtualMachineProvisioningCheckerApi.md#virtual_machine_provisioning_checker_check_migrate_task) | **POST** /VirtualMachineProvisioningChecker/{moId}/CheckMigrate_Task | Tests the feasibility of a proposed *VirtualMachine.MigrateVM_Task* operation. 
[**virtual_machine_provisioning_checker_check_relocate_task**](VirtualMachineProvisioningCheckerApi.md#virtual_machine_provisioning_checker_check_relocate_task) | **POST** /VirtualMachineProvisioningChecker/{moId}/CheckRelocate_Task | Tests the feasibility of a proposed *VirtualMachine.RelocateVM_Task* operation. 
[**virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task**](VirtualMachineProvisioningCheckerApi.md#virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task) | **POST** /VirtualMachineProvisioningChecker/{moId}/QueryVMotionCompatibilityEx_Task | Investigates the general VMotion compatibility of a set of virtual machines with a set of hosts. 


# **virtual_machine_provisioning_checker_check_clone_task**
> ManagedObjectReference virtual_machine_provisioning_checker_check_clone_task(mo_id, check_clone_request_type)

Tests the feasibility of a proposed *VirtualMachine.CloneVM_Task* operation. 

Tests the feasibility of a proposed *VirtualMachine.CloneVM_Task* operation.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_clone_request_type import CheckCloneRequestType
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
    api_instance = vmware_vi.VirtualMachineProvisioningCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_clone_request_type = vmware_vi.CheckCloneRequestType() # CheckCloneRequestType | 

    try:
        # Tests the feasibility of a proposed *VirtualMachine.CloneVM_Task* operation. 
        api_response = api_instance.virtual_machine_provisioning_checker_check_clone_task(mo_id, check_clone_request_type)
        print("The response of VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_clone_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_clone_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_clone_request_type** | [**CheckCloneRequestType**](CheckCloneRequestType.md)|  | 

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
**500** | ***InvalidArgument***: in the following cases: - the target host and target pool are not associated with the   same compute resource - the target pool represents a cluster without DRS enabled,   and the host is not specified - Datastore in a diskLocator entry is not specified - the specified device ID cannot be found in the virtual machine&#39;s current   configuration - the object specified in relocate cannot be found - the target pool is not specified while checking feasibility of   cloning to a different datacenter or a different vCenter   service - the datastore is not specified when testType parameter includes   datastore tests while checking feasibility of cloning to a   different datacenter or a different vCenter service    ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_provisioning_checker_check_instant_clone_task**
> ManagedObjectReference virtual_machine_provisioning_checker_check_instant_clone_task(mo_id, check_instant_clone_request_type)

Tests the feasibility of a proposed *VirtualMachine.InstantClone_Task* operation. 

Tests the feasibility of a proposed *VirtualMachine.InstantClone_Task* operation.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_instant_clone_request_type import CheckInstantCloneRequestType
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
    api_instance = vmware_vi.VirtualMachineProvisioningCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_instant_clone_request_type = vmware_vi.CheckInstantCloneRequestType() # CheckInstantCloneRequestType | 

    try:
        # Tests the feasibility of a proposed *VirtualMachine.InstantClone_Task* operation. 
        api_response = api_instance.virtual_machine_provisioning_checker_check_instant_clone_task(mo_id, check_instant_clone_request_type)
        print("The response of VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_instant_clone_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_instant_clone_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_instant_clone_request_type** | [**CheckInstantCloneRequestType**](CheckInstantCloneRequestType.md)|  | 

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
**500** | ***InvalidArgument***: in the following cases: - The destination host does not support Instant Clone. - The source and destination host are not the same. - The relocate spec in the Instant Clone spec has   Datastore set. - The relocate spec in the Instant Clone spec has host set. - The Instant clone spec does not have name set. - The source VM is a template. - The source VM is not powered on. - The source VM has PMEM devices/disks configured.    ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_provisioning_checker_check_migrate_task**
> ManagedObjectReference virtual_machine_provisioning_checker_check_migrate_task(mo_id, check_migrate_request_type)

Tests the feasibility of a proposed *VirtualMachine.MigrateVM_Task* operation. 

Tests the feasibility of a proposed *VirtualMachine.MigrateVM_Task* operation.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_migrate_request_type import CheckMigrateRequestType
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
    api_instance = vmware_vi.VirtualMachineProvisioningCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_migrate_request_type = vmware_vi.CheckMigrateRequestType() # CheckMigrateRequestType | 

    try:
        # Tests the feasibility of a proposed *VirtualMachine.MigrateVM_Task* operation. 
        api_response = api_instance.virtual_machine_provisioning_checker_check_migrate_task(mo_id, check_migrate_request_type)
        print("The response of VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_migrate_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_migrate_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_migrate_request_type** | [**CheckMigrateRequestType**](CheckMigrateRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if the target host(s) and target pool for a migration are not associated with the same compute resource, or if the host parameter is left unset when the target pool is associated with a non-DRS cluster.  ***InvalidPowerState***: if the state argument is set and at least one of the specified virtual machines is not in that power state.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_provisioning_checker_check_relocate_task**
> ManagedObjectReference virtual_machine_provisioning_checker_check_relocate_task(mo_id, check_relocate_request_type)

Tests the feasibility of a proposed *VirtualMachine.RelocateVM_Task* operation. 

Tests the feasibility of a proposed *VirtualMachine.RelocateVM_Task* operation.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_relocate_request_type import CheckRelocateRequestType
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
    api_instance = vmware_vi.VirtualMachineProvisioningCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_relocate_request_type = vmware_vi.CheckRelocateRequestType() # CheckRelocateRequestType | 

    try:
        # Tests the feasibility of a proposed *VirtualMachine.RelocateVM_Task* operation. 
        api_response = api_instance.virtual_machine_provisioning_checker_check_relocate_task(mo_id, check_relocate_request_type)
        print("The response of VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_relocate_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_check_relocate_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_relocate_request_type** | [**CheckRelocateRequestType**](CheckRelocateRequestType.md)|  | 

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
**500** | ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidArgument***: in the following cases: - the target host and target pool are not associated with the   same compute resource - the target pool represents a cluster without DRS enabled,   and the host is not specified - Datastore in a diskLocator entry is not specified - the specified device ID cannot be found in the virtual machine&#39;s current   configuration - the object specified in relocate cannot be found - the target pool is not specified while checking feasibility of   relocation to a different datacenter or different vCenter   service - the datastore is not specified when testType parameter includes   datastore tests while checking feasibility of relocation to a   different datacenter or a different vCenter service    ***InvalidState***: if the operation cannot be performed because of the host or virtual machine&#39;s current state. For example, if the host is in maintenance mode, or if the virtual machine&#39;s configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task**
> ManagedObjectReference virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task(mo_id, query_v_motion_compatibility_ex_request_type)

Investigates the general VMotion compatibility of a set of virtual machines with a set of hosts. 

Investigates the general VMotion compatibility of a set of virtual machines with a set of hosts.  The virtual machine may be in any power state. Hosts may be in any connection state and also may be in maintenance mode.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_v_motion_compatibility_ex_request_type import QueryVMotionCompatibilityExRequestType
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
    api_instance = vmware_vi.VirtualMachineProvisioningCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_v_motion_compatibility_ex_request_type = vmware_vi.QueryVMotionCompatibilityExRequestType() # QueryVMotionCompatibilityExRequestType | 

    try:
        # Investigates the general VMotion compatibility of a set of virtual machines with a set of hosts. 
        api_response = api_instance.virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task(mo_id, query_v_motion_compatibility_ex_request_type)
        print("The response of VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineProvisioningCheckerApi->virtual_machine_provisioning_checker_query_v_motion_compatibility_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_v_motion_compatibility_ex_request_type** | [**QueryVMotionCompatibilityExRequestType**](QueryVMotionCompatibilityExRequestType.md)|  | 

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

