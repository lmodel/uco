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
  A contact affiliation is a grouping of characteristics unique to details of an organizational affiliation for a single contact entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactAffiliation extends UcoInherentCharacterizationThing {

  private List<ContactEmail> contactEmail;
  private List<ContactMessaging> contactMessaging;
  private Organization contactOrganization;
  private List<ContactPhone> contactPhone;
  private List<ContactProfile> contactProfile;
  private List<ContactURL> contactURL;
  private String organizationDepartment;
  private List<ContactAddress> organizationLocation;
  private String organizationPosition;


}