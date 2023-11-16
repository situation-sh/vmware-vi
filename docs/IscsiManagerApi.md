# vmware_vi.IscsiManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iscsi_manager_bind_vnic**](IscsiManagerApi.md#iscsi_manager_bind_vnic) | **POST** /IscsiManager/{moId}/BindVnic | Bind a Virtual NIC to be used for an iSCSI adapter 
[**iscsi_manager_query_bound_vnics**](IscsiManagerApi.md#iscsi_manager_query_bound_vnics) | **POST** /IscsiManager/{moId}/QueryBoundVnics | Query the list of Virtual NICs that are bound to a given iSCSI HBA. 
[**iscsi_manager_query_candidate_nics**](IscsiManagerApi.md#iscsi_manager_query_candidate_nics) | **POST** /IscsiManager/{moId}/QueryCandidateNics | Query the candidate Virtual NICs and Physical NICs that can be used for Port-Binding. 
[**iscsi_manager_query_migration_dependencies**](IscsiManagerApi.md#iscsi_manager_query_migration_dependencies) | **POST** /IscsiManager/{moId}/QueryMigrationDependencies | Query the dependency table for a migration operation of a given Physical NIC. 
[**iscsi_manager_query_pnic_status**](IscsiManagerApi.md#iscsi_manager_query_pnic_status) | **POST** /IscsiManager/{moId}/QueryPnicStatus | Query if Physical NIC device is used for iSCSI. 
[**iscsi_manager_query_vnic_status**](IscsiManagerApi.md#iscsi_manager_query_vnic_status) | **POST** /IscsiManager/{moId}/QueryVnicStatus | Query the status of Virtual NIC association with the iSCSI. 
[**iscsi_manager_unbind_vnic**](IscsiManagerApi.md#iscsi_manager_unbind_vnic) | **POST** /IscsiManager/{moId}/UnbindVnic | Unbind Virtual NIC binding from an iSCSI adapter. 


# **iscsi_manager_bind_vnic**
> iscsi_manager_bind_vnic(mo_id, bind_vnic_request_type)

Bind a Virtual NIC to be used for an iSCSI adapter 

Bind a Virtual NIC to be used for an iSCSI adapter  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.bind_vnic_request_type import BindVnicRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    bind_vnic_request_type = vmware_vi.BindVnicRequestType() # BindVnicRequestType | 

    try:
        # Bind a Virtual NIC to be used for an iSCSI adapter 
        api_instance.iscsi_manager_bind_vnic(mo_id, bind_vnic_request_type)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_bind_vnic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **bind_vnic_request_type** | [**BindVnicRequestType**](BindVnicRequestType.md)|  | 

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
**500** | ***IscsiFaultVnicAlreadyBound***: The given Virtual NIC is already bound to the HBA.  ***IscsiFaultVnicHasNoUplinks***: The given Virtual NIC has no physical uplinks.  ***IscsiFaultVnicHasMultipleUplinks***: The given Virtual NIC has multiple uplinks.  ***IscsiFaultVnicHasWrongUplink***: The given Virtual NIC has the wrong uplink and it can&#39;t be used for iSCSI multi-pathing.  ***IscsiFaultVnicNotFound***: The given Virtual NIC is not present on the system.  ***IscsiFaultInvalidVnic***: The given Virtual NIC is not valid for the HBA.  ***PlatformConfigFault***: For platform error that occurs during the operation.  ***IscsiFault***: For any problem that is not handled with a more specific fault.  ***NotFound***: If the given HBA is not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_query_bound_vnics**
> List[IscsiPortInfo] iscsi_manager_query_bound_vnics(mo_id, query_bound_vnics_request_type)

Query the list of Virtual NICs that are bound to a given iSCSI HBA. 

Query the list of Virtual NICs that are bound to a given iSCSI HBA.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.iscsi_port_info import IscsiPortInfo
from vmware_vi.models.query_bound_vnics_request_type import QueryBoundVnicsRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_bound_vnics_request_type = vmware_vi.QueryBoundVnicsRequestType() # QueryBoundVnicsRequestType | 

    try:
        # Query the list of Virtual NICs that are bound to a given iSCSI HBA. 
        api_response = api_instance.iscsi_manager_query_bound_vnics(mo_id, query_bound_vnics_request_type)
        print("The response of IscsiManagerApi->iscsi_manager_query_bound_vnics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_query_bound_vnics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_bound_vnics_request_type** | [**QueryBoundVnicsRequestType**](QueryBoundVnicsRequestType.md)|  | 

### Return type

[**List[IscsiPortInfo]**](IscsiPortInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of *IscsiPortInfo* containing detailed information on the list of Virtual NICs bound to the adapter  |  -  |
**500** | ***IscsiFault***: For any problem that is not handled with a more specific fault.  ***NotFound***: If the given HBA is not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_query_candidate_nics**
> List[IscsiPortInfo] iscsi_manager_query_candidate_nics(mo_id, query_candidate_nics_request_type)

Query the candidate Virtual NICs and Physical NICs that can be used for Port-Binding. 

Query the candidate Virtual NICs and Physical NICs that can be used for Port-Binding.  For dependent offload adapters, the Virtual NIC should be attached to the physical NIC associated with the hardware function.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.iscsi_port_info import IscsiPortInfo
from vmware_vi.models.query_candidate_nics_request_type import QueryCandidateNicsRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_candidate_nics_request_type = vmware_vi.QueryCandidateNicsRequestType() # QueryCandidateNicsRequestType | 

    try:
        # Query the candidate Virtual NICs and Physical NICs that can be used for Port-Binding. 
        api_response = api_instance.iscsi_manager_query_candidate_nics(mo_id, query_candidate_nics_request_type)
        print("The response of IscsiManagerApi->iscsi_manager_query_candidate_nics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_query_candidate_nics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_candidate_nics_request_type** | [**QueryCandidateNicsRequestType**](QueryCandidateNicsRequestType.md)|  | 

### Return type

[**List[IscsiPortInfo]**](IscsiPortInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of *IscsiPortInfo* containing detailed information on list of eligible Virtual NICs that can be bound to the adapter. This list will also include details on the eligible Physical NICs that are not associated with any Virtual NICs.  |  -  |
**500** | ***IscsiFault***: For any problem that is not handled with a more specific fault.  ***NotFound***: If the given HBA is not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_query_migration_dependencies**
> IscsiMigrationDependency iscsi_manager_query_migration_dependencies(mo_id, query_migration_dependencies_request_type)

Query the dependency table for a migration operation of a given Physical NIC. 

Query the dependency table for a migration operation of a given Physical NIC.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.iscsi_migration_dependency import IscsiMigrationDependency
from vmware_vi.models.query_migration_dependencies_request_type import QueryMigrationDependenciesRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_migration_dependencies_request_type = vmware_vi.QueryMigrationDependenciesRequestType() # QueryMigrationDependenciesRequestType | 

    try:
        # Query the dependency table for a migration operation of a given Physical NIC. 
        api_response = api_instance.iscsi_manager_query_migration_dependencies(mo_id, query_migration_dependencies_request_type)
        print("The response of IscsiManagerApi->iscsi_manager_query_migration_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_query_migration_dependencies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_migration_dependencies_request_type** | [**QueryMigrationDependenciesRequestType**](QueryMigrationDependenciesRequestType.md)|  | 

### Return type

[**IscsiMigrationDependency**](IscsiMigrationDependency.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dependency table, as described in *IscsiMigrationDependency*, providing the user of all the Virtual NIC and iSCSI resources affected.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_query_pnic_status**
> IscsiStatus iscsi_manager_query_pnic_status(mo_id, query_pnic_status_request_type)

Query if Physical NIC device is used for iSCSI. 

Query if Physical NIC device is used for iSCSI.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.iscsi_status import IscsiStatus
from vmware_vi.models.query_pnic_status_request_type import QueryPnicStatusRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_pnic_status_request_type = vmware_vi.QueryPnicStatusRequestType() # QueryPnicStatusRequestType | 

    try:
        # Query if Physical NIC device is used for iSCSI. 
        api_response = api_instance.iscsi_manager_query_pnic_status(mo_id, query_pnic_status_request_type)
        print("The response of IscsiManagerApi->iscsi_manager_query_pnic_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_query_pnic_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_pnic_status_request_type** | [**QueryPnicStatusRequestType**](QueryPnicStatusRequestType.md)|  | 

### Return type

[**IscsiStatus**](IscsiStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object, *IscsiStatus*, indicating whether Physical NIC is used by iSCSI or not. - Empty *IscsiStatus* (i.e reason unset)   if Physical NIC device is not used. - Fault code *IscsiFaultPnicInUse* if   Physical NIC is being used.  |  -  |
**500** | ***IscsiFault***: For any problem that is not handled with a more specific fault.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_query_vnic_status**
> IscsiStatus iscsi_manager_query_vnic_status(mo_id, query_vnic_status_request_type)

Query the status of Virtual NIC association with the iSCSI. 

Query the status of Virtual NIC association with the iSCSI.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.iscsi_status import IscsiStatus
from vmware_vi.models.query_vnic_status_request_type import QueryVnicStatusRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vnic_status_request_type = vmware_vi.QueryVnicStatusRequestType() # QueryVnicStatusRequestType | 

    try:
        # Query the status of Virtual NIC association with the iSCSI. 
        api_response = api_instance.iscsi_manager_query_vnic_status(mo_id, query_vnic_status_request_type)
        print("The response of IscsiManagerApi->iscsi_manager_query_vnic_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_query_vnic_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vnic_status_request_type** | [**QueryVnicStatusRequestType**](QueryVnicStatusRequestType.md)|  | 

### Return type

[**IscsiStatus**](IscsiStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object *IscsiStatus*, containing list of the fault codes, providing the user with information as to whether Virtual NIC is used by iSCSI and list of compliance check failure codes if any. The returned *IscsiStatus* object will have an array of *MethodFault* objects providing following information: - Empty *IscsiStatus* (i.e reason unset)   if Virtual NIC device is not used. - Fault code *IscsiFaultVnicInUse* if Virtual   NIC is being used by iSCSI. - This will be followed with list of fault codes   corresponding to the compliance check failures.  |  -  |
**500** | ***IscsiFault***: For any problem that is not handled with a more specific fault.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iscsi_manager_unbind_vnic**
> iscsi_manager_unbind_vnic(mo_id, unbind_vnic_request_type)

Unbind Virtual NIC binding from an iSCSI adapter. 

Unbind Virtual NIC binding from an iSCSI adapter.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unbind_vnic_request_type import UnbindVnicRequestType
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
    api_instance = vmware_vi.IscsiManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unbind_vnic_request_type = vmware_vi.UnbindVnicRequestType() # UnbindVnicRequestType | 

    try:
        # Unbind Virtual NIC binding from an iSCSI adapter. 
        api_instance.iscsi_manager_unbind_vnic(mo_id, unbind_vnic_request_type)
    except Exception as e:
        print("Exception when calling IscsiManagerApi->iscsi_manager_unbind_vnic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unbind_vnic_request_type** | [**UnbindVnicRequestType**](UnbindVnicRequestType.md)|  | 

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
**500** | ***IscsiFaultVnicNotBound***: The given Virtual NIC is not bound to the adapter  ***IscsiFaultVnicHasActivePaths***: The given Virtual NIC is associated with \&quot;active\&quot; paths to the storage.  ***IscsiFaultVnicIsLastPath***: The given Virtual NIC is associated with \&quot;only\&quot; paths to the storage.  ***PlatformConfigFault***: For platform error that occurs during the operation.  ***IscsiFault***: For any problem that is not handled with a more specific fault.  ***NotFound***: If the given HBA is not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

