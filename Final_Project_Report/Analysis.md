# **FINAL PROJECT ANALYSIS REPORT**

### *A Cross-Platform Analysis of Spotify & YouTube Engagement*

### **Nguyen My San – MSBA 285 Capstone Project**

### Eberhardt School of Business, University of the Pacific

---

## **1. Introduction**

The streaming economy has transformed how music is consumed globally. This project analyzes **Spotify** and **YouTube engagement metrics** to identify music trends, artist performance, and cross-platform behavior.

Using a curated dataset of **1,527 artists** and **3,401 tracks** (1987–2024), SQL (BigQuery), and Grafana, this dashboard evaluates:

* Spotify Streams
* Spotify Popularity Scores
* YouTube Likes
* Shazam Counts
* Artist & Track Rankings

This cross-platform approach provides deeper insight into global fan engagement and digital music consumption.

---

## **2. Dataset Overview**

The dataset includes:

* **Total Artists:** 1,527
* **Total Tracks:** 3,401
* **Date Range:** 1987–2024
* **Features:** Streams, Popularity, Shazam counts, YouTube Views & Likes, Artists, Tracks, Release Years

### **📌 Screenshot Placeholder**

![Dataset Overview Screenshot](Dashboard_Screenshots/dataset_overview.png)


---

## **3. Dashboard Panel Analysis**

---

### **3.1 Total Artists & Tracks Panel**

Shows the size of the dataset used in this study.
**Insight:** A large sample of artists and songs allows for reliable global trend analysis.

### **📌 Screenshot Placeholder**

![Total Artists Panel](Dashboard_Screenshots/Total_Artists.png)

![Total Tracks Panel](Dashboard_Screenshots/Total_Tracks.png)


---

### **3.2 Average Spotify Popularity Over Time (Line Chart)**

Displays how average track popularity changed from 1987 to 2024.

**Findings:**

* Popularity is mostly stable with certain upward jumps from viral songs.
* Peaks often correspond to major global releases or platform-wide social media trends.

### **📌 Screenshot Placeholder**

![Average Spotify Popularity Over Time](Dashboard_Screenshots/AVG_Spotify_Popularity.png)


---

### **3.3 Spotify Streams vs. YouTube Views (Trend Chart)**

This comparison reveals long-term Spotify engagement vs. short-term YouTube virality.

**Insight:**

* **YouTube** shows sharp engagement spikes during viral moments.
* **Spotify** reflects consistent listener retention over time.

### **📌 Screenshot Placeholder**

![Spotify Streams vs YouTube Views](Dashboard_Screenshots/SpotifyStreams_VS_YTViews.png)


---

### **3.4 YouTube Likes by Artist – Top 10 (Bar Chart)**

Ranks artists with the highest YouTube engagement.

**Top performers include:**

* **BTS** – 330M likes
* **BLACKPINK** – 245M
* **Ariana Grande** – 176M
* **Bad Bunny** – 155M
* **Justin Bieber** – 144M

**Insight:** K-pop groups sustain extremely high global digital engagement.

### **📌 Screenshot Placeholder**

![Top Artists by YouTube Likes](Dashboard_Screenshots/TOPARTISTSBYYTLIKES.png)


---

### **3.5 Total Spotify Streams by Artist – Top 10 (Bar Chart)**

Displays artists with the highest lifetime Spotify streams.

**Insight:** Top artists maintain long-term streaming success through global audience reach and brand strength.

### **📌 Screenshot Placeholder**

![Top Artists by Total Spotify Streams](Dashboard_Screenshots/TOTAL_SPOTIFY_STREAMS_BY_ARTIST.png)



---

### **3.6 Artist–Track Popularity Histogram**

Shows distribution of track popularity scores.

**Insight:**

* Most tracks fall between **popularity scores 40–70**, showing balanced listening behaviors.
* Extremely low or extremely high popularity scores are rare.

### **📌 Screenshot Placeholder**

![Artist–Track Popularity Histogram](Dashboard_Screenshots/HISTOGRAM.png)


---

### **3.7 Average YouTube Likes by Artist – Top 10**

Measures fan engagement outside Spotify.

**Insight:** Viral children's content (e.g., **Pinkfong**) performs exceptionally well.
High YouTube activity often correlates with long-term Spotify streaming.

### **📌 Screenshot Placeholder**

![Average YouTube Likes by Artist](Dashboard_Screenshots/AVG_YT_LIKESBY_ARTIST.png)


---

### **3.8 Top 10 Most Popular Tracks (Table)**

Displays highest Spotify popularity scores.

**Top tracks include:**

* *A Bar Song (Tipsy)* – Shaboozey (Score: 96)
* *Espresso* – Sabrina Carpenter (Score: 95)

**Insight:** These tracks reflect strong listener engagement and social media influence.

### **📌 Screenshot Placeholder**

![Top 10 Most Popular Spotify Tracks](Dashboard_Screenshots/TOP10_MOSTPOPULARTRACKSFROMSPOTIFY.png)


---

## **4. Key Findings**

* Spotify popularity remains stable but is influenced by major releases and viral trends.
* YouTube likes strongly correlate with short-term popularity spikes.
* Spotify streams represent consistent long-term listening behavior.
* K-pop acts and U.S. megastars dominate both platforms.
* Shazam, YouTube Likes, and Spotify Streams together predict overall popularity.

---

## **5. Conclusion**

This project demonstrates how integrating Spotify and YouTube data reveals deeper insights into global digital music consumption.

The Grafana dashboard:

* Visualizes multi-platform engagement
* Highlights global streaming patterns
* Identifies trends in music discovery and fan behavior

This analysis is valuable for music producers, marketers, streaming platforms, and artists seeking to understand their audience.

---

## **6. Appendix (Screenshot Placeholders)**

Use this area to insert final screenshots.

```
### Dashboard Overview  
![Dashboard Overview](ADD_IMAGE_HERE)

### Data Cleaning Steps  
![Data Cleaning](ADD_IMAGE_HERE)

### SQL Queries Used  
![SQL Code](ADD_IMAGE_HERE)

### Grafana Panels  
![Grafana Panel Screenshot](ADD_IMAGE_HERE)
```

---

**End of Report**
