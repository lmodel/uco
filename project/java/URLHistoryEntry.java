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
  A URL history entry is a grouping of characteristics unique to the properties of a single URL history entry for a particular browser.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLHistoryEntry extends UcoInherentCharacterizationThing {

  private String browserUserProfile;
  private ZonedDateTime expirationTime;
  private ZonedDateTime firstVisit;
  private String hostname;
  private List<String> keywordSearchTerm;
  private ZonedDateTime lastVisit;
  private Integer manuallyEnteredCount;
  private String pageTitle;
  private List<ObservableObject> referrerUrl;
  private ObservableObject url;
  private Integer visitCount;


}