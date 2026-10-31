package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A Windows Active Directory account facet is a grouping of characteristics unique to an account managed by directory-based identity-related services of a Windows operating system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsActiveDirectoryAccountFacet extends Facet {

  private List<String> activeDirectoryGroups;
  private String objectGUID;


}