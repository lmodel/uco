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
  A contact facet is a grouping of characteristics unique to a set of identification and communication related details for a single entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactFacet extends Facet {

  private ZonedDateTime birthdate;
  private List<ContactAddress> contactAddress;
  private List<ContactAffiliation> contactAffiliation;
  private List<ContactEmail> contactEmail;
  private List<String> contactGroup;
  private String contactID;
  private List<ContactMessaging> contactMessaging;
  private List<String> contactNote;
  private List<ContactPhone> contactPhone;
  private List<ContactProfile> contactProfile;
  private List<ContactSIP> contactSIP;
  private List<ContactURL> contactURL;
  private String displayName;
  private String firstName;
  private String lastName;
  private ZonedDateTime lastTimeContacted;
  private String middleName;
  private String namePhonetic;
  private String namePrefix;
  private String nameSuffix;
  private List<String> nickname;
  private Integer numberTimesContacted;
  private ObservableObject sourceApplication;


}